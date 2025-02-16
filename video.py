from pydub import AudioSegment
from moviepy import ImageSequenceClip, AudioFileClip, concatenate_videoclips, TextClip, CompositeVideoClip
import file_util
import random
from concurrent.futures import ThreadPoolExecutor, as_completed

def concatenate_audio_files_with_background(
    audio_paths, 
    background_audio_path, 
    output_audio_path=None, 
    background_volume=-20, 
    crossfade_duration=1000, 
    truncate_start=3, 
    truncate_end=3
):
    """
    Concatenate multiple audio files into a single audio file with a background track.
    Track the start times of each original audio segment in the final file.

    :param audio_paths: List of paths to the audio files.
    :param background_audio_path: Path to the background audio file.
    :param output_audio_path: Path to save the concatenated audio file.
    :param background_volume: Volume of the background track (in dB). Default is -20 dB.
    :param crossfade_duration: Duration of the crossfade between audio tracks (in milliseconds). Default is 1000 ms.
    :param truncate_start: Duration to truncate from the start of each audio segment (in milliseconds). Default is 3 ms.
    :param truncate_end: Duration to truncate from the end of each audio segment (in milliseconds). Default is 3 ms.
    :return: A list of tuples containing (audio_file, start_time) for each segment.
    """

    combined_audio = AudioSegment.empty()

    start_times = []
    current_time = 0
    random.shuffle(audio_paths)
    for i, audio_file in enumerate(audio_paths):
        print(f'Starting on audio path-{i}: {audio_file}')
        audio = AudioSegment.from_file(audio_file)

        # Truncate the start and end of the audio segment
        if truncate_start > 0:
            audio = audio[truncate_start:]
        if truncate_end > 0:
            audio = audio[:-truncate_end]

        # Apply crossfade if it's not the first audio segment
        if i > 0:
            combined_audio = combined_audio.append(audio, crossfade=crossfade_duration)
        else:
            combined_audio += audio

        start_times.append((audio_file, current_time))
        current_time += len(audio) - (crossfade_duration if i > 0 else 0)

    if background_audio_path != None:
        background_audio = AudioSegment.from_file(background_audio_path)
        background_audio = background_audio + background_volume
        background_audio = background_audio * (len(combined_audio) // len(background_audio) + 1)
        background_audio = background_audio[:len(combined_audio)]

        final_audio = combined_audio.overlay(background_audio)
        final_audio.export(output_audio_path, format="mp3")
    else:
        combined_audio.export(output_audio_path, format="mp3")

    return start_times

def get_background_music_if_exists(source_root_path):
    background_music_filenames = file_util.get_files_with_extension(source_root_path + f'background_music/', 'mp3')
    if background_music_filenames != None and len(background_music_filenames) > 0:
        return background_music_filenames[0]
    return None

def create_video_with_images_and_audio(
    project_name, 
    fps=1, 
    background_volume=-20, 
    crossfade_duration=1000, 
    truncate_start=3, 
    truncate_end=3,
    overlay_duration=3,  # Duration of the track name overlay in seconds
    font_size=30,        # Font size of the track name
    font_color="green",  # Color of the track name text
    font='/mnt/c/Windows/Fonts/cour.ttf',      # Monospace font for terminal-style text
    cover_image_path=None  # Path to the cover image
):
    """
    Create a video that changes images at the start of every audio file, overlays the track name, and includes a cover image.

    :param fps: Frames per second for the video.
    :param background_volume: Volume of the background track (in dB). Default to -20 dB.
    :param crossfade_duration: Duration of the crossfade between audio tracks (in milliseconds). Default is 1000 ms.
    :param truncate_start: Duration to truncate from the start of each audio segment (in milliseconds). Default is 3 ms.
    :param truncate_end: Duration to truncate from the end of each audio segment (in milliseconds). Default is 3 ms.
    :param overlay_duration: Duration of the track name overlay (in seconds). Default is 3 seconds.
    :param font_size: Font size of the track name. Default is 30.
    :param font_color: Color of the track name text. Default is "white".
    :param font: Font family for the text. Default is "Courier" (monospace).
    :param cover_image_path: Path to the cover image. Default is None.
    """
    source_root_path = f'projects/{project_name}/'

    source_audio_path = source_root_path + 'audio'
    audio_paths = file_util.get_files_with_extension(source_audio_path, 'mp3')
    print(f'got {len(audio_paths)} files from {source_audio_path}')
    source_background_music_path = get_background_music_if_exists(source_root_path)

    source_image_path = source_root_path + 'images'
    image_paths = file_util.get_files_with_extension(source_image_path, 'png')
    random.shuffle(image_paths)

    output_audio_path = source_root_path + "temp/temp_combined_audio.mp3"
    output_video_path = source_root_path + f'output/{project_name}.mp4'
    
    start_times = concatenate_audio_files_with_background(
        audio_paths, 
        source_background_music_path, 
        output_audio_path, 
        background_volume, 
        crossfade_duration, 
        truncate_start, 
        truncate_end
    )

    clips = []
    for i, (audio_file, _) in enumerate(start_times):
        print(f'Starting video segment-{i}: {audio_file}')
        if i < len(start_times) - 1:
            duration = (start_times[i + 1][1] - start_times[i][1]) / 1000  # Convert to seconds
        else:
            duration = (AudioSegment.from_file(audio_file).duration_seconds)

        # Create the image clip
        image_clip = ImageSequenceClip([image_paths[i]], durations=[duration])

        # Create the track name overlay
        track_name = ' '.join(audio_file.split('/')[-1].split('.')[0].split('_'))
        print(track_name)
        text_clip = TextClip(
            text=track_name, 
            font_size=font_size, 
            color=font_color,
            margin=(20, 20),
            font=font,
            bg_color='black',
        ).with_position(("center", "center")).with_duration(overlay_duration).with_start(0)

        # Add cover image if provided
        if cover_image_path and i == 0:  # Only add the cover image to the first segment
            cover_clip = ImageSequenceClip([cover_image_path], durations=[overlay_duration])
            cover_clip = cover_clip.resize(height=image_clip.size[1])  # Resize cover to match video height
            cover_clip = cover_clip.set_position(("center", "center"))

            # Combine the image clip, cover, and text overlay
            composite_clip = CompositeVideoClip([image_clip, cover_clip, text_clip])
        else:
            # Combine the image clip and text overlay
            composite_clip = CompositeVideoClip([image_clip, text_clip])

        clips.append(composite_clip)

    # Concatenate all clips into the final video
    final_video = concatenate_videoclips(clips)

    # Add the combined audio to the video
    final_audio = AudioFileClip(output_audio_path)
    final_video = final_video.with_audio(final_audio)

    # Write the final video to a file
    final_video.write_videofile(output_video_path, codec="libx264", fps=fps)

    print(f"Final video saved to {output_video_path}")