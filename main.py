from args import ArgParser
import video
import file_util

def main():
    if args.project:
        project = args.project
        file_util.ensure_folders_exist(project)
        video.create_video_with_images_and_audio(project)
    else:
        file_util.ensure_folders_exist(args.newProject, new=True)

if __name__ == "__main__":
    args = ArgParser().get_args()
    main()
