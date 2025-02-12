from pydub import AudioSegment
from moviepy import ImageSequenceClip, AudioFileClip, concatenate_videoclips
import file_util
def concatenate_audio_files_with_background(audio_paths, background_audio_path, output_audio_path=None, background_volume=-20):
    """
    Concatenate multiple audio files into a single audio file with a background track.
    Track the start times of each original audio segment in the final file.

    :param audio_paths: List of paths to the audio files.
    :param background_audio_path: Path to the background audio file.
    :param output_audio_path: Path to save the concatenated audio file.
    :param background_volume: Volume of the background track (in dB). Default is -20 dB.
    :return: A list of tuples containing (audio_file, start_time) for each segment.
    """

    combined_audio = AudioSegment.empty()

    start_times = []
    current_time = 0

    for audio_file in audio_paths:
        audio = AudioSegment.from_file(audio_file)
        start_times.append((audio_file, current_time))
        combined_audio += audio
        current_time += len(audio)

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

def create_video_with_images_and_audio(project_name, fps=1, background_volume=-20):
    """
    Create a video that changes images at the start of every audio file.

    :param fps: Frames per second for the video.
    :param background_volume: Volume of the background track (in dB). Default to -20 dB.
    """
    source_root_path = f'projects/{project_name}/'

    source_audio_path = source_root_path + 'audio/'
    audio_paths = file_util.get_files_with_extension(source_audio_path, 'mp3')

    source_background_music_path = get_background_music_if_exists(source_root_path)

    source_image_path = source_root_path + 'images/'
    image_paths = file_util.get_files_with_extension(source_image_path, 'webp')
    
    output_audio_path = source_root_path + "temp/temp_combined_audio.mp3"
    output_video_path = source_root_path + f'output/{project_name}.mp4'
    
    start_times = concatenate_audio_files_with_background(audio_paths, source_background_music_path, output_audio_path, background_volume)


    clips = []
    for i, (audio_file, _) in enumerate(start_times):
        if i < len(start_times) - 1:
            duration = (start_times[i + 1][1] - start_times[i][1]) / 1000  # Convert to seconds
        else:
            duration = (AudioSegment.from_file(audio_file).duration_seconds)

        image_clip = ImageSequenceClip([image_paths[i]], durations=[duration])
        clips.append(image_clip)

    final_video = concatenate_videoclips(clips)

    final_audio = AudioFileClip(output_audio_path)
    final_video = final_video.with_audio(final_audio)

    final_video.write_videofile(output_video_path, codec="libx264", fps=fps)

    print(f"Final video saved to {output_video_path}")