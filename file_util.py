import os

class Folder:
    def __init__(self, path, purpose):
        self.path = path
        self.purpose = purpose

def get_files_with_extension(folder_path, extension):
    """
    Returns a list of files in the specified folder with the given extension.

    :param folder_path: Path to the folder to search in.
    :param extension: The file extension to filter by (e.g., '.txt', '.jpg').
    :return: A list of file names with the specified extension.
    """
    # Ensure the extension starts with a dot
    if not extension.startswith('.'):
        extension = '.' + extension

    # List all files in the folder
    try:
        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    except FileNotFoundError:
        print(f"The folder '{folder_path}' does not exist.")
        return []

    # Filter files by the specified extension
    filtered_files = [folder_path + '/' + f for f in files if f.endswith(extension)]

    return filtered_files

def ensure_folder_exists(folder, new=False):
    """
    Checks if a folder exists, and creates it if it doesn't.

    :param folder_path: Path to the folder to check or create.
    """
    if not os.path.exists(folder.path):
        os.makedirs(folder.path)
        if new:
            print(f"Folder '{folder.path}' created.")
            print(f"{folder.purpose}")
    elif new:
        print(f"Folder '{folder.path}' already exists.")
        print(f" - {folder.purpose}")

def ensure_folders_exist(project_name, new=False):
    project_root = Folder(f'projects/{project_name}/', 'Holds the whole project, each subfolder contains items of one type')
    source_audio = Folder(project_root.path + 'audio/', 'Holds all of the audio files, ensure that the files you place in here are sortable alphabetically otherwise you may end up with audio out of order')
    source_background_music = Folder(project_root.path + 'Background_music/', 'Put one file in this folder to be used as background music')
    source_image = Folder(project_root.path + 'images/', 'Put all images in this folder to be used as background images and make sure they are sortable alphabetically')
    output = Folder(project_root.path + 'output/', 'Destination folder for the output video')
    temp = Folder(project_root.path + 'temp/', 'Used to hold the background music/audio combo file before creating video')
    if not os.path.exists(project_root.path):
        ensure_folder_exists(project_root, new)
    elif new:
        print('project folder already exists, ensuring subfolders exist')
    folder_paths = [source_audio, source_background_music, source_image, output, temp]
    for folder_path in folder_paths:
        ensure_folder_exists(folder_path, new)