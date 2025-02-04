
# vidipy

python library that makes videos using static images and audio
# installation 
```
git clone git@github.com:pnixon/vidipy.git vidipy
cd vidipy
pip install -r requirements.txt
```
# example project
an example project is already in the repo, to run this on that project simply run the following command
```
python main.py -p example_project
 ```
# How it works
It is built as a wrapper/utility around the moviepy library.

The basic idea is to create videos using static images and audio without having to bother with annoying UI's.

## to create a new project
`python main.py -n project_name`
- will create a project with name project_name and show the following output
```
python main.py -n project_name
Folder 'projects/project_name/' created.
Holds the whole project, each subfolder contains items of one type
Folder 'projects/project_name/audio/' created.
Holds all of the audio files, ensure that the files you place in here are sortable alphabetically otherwise you may end up with audio out of order
Folder 'projects/project_name/Background_music/' created.
Put one file in this folder to be used as background music
Folder 'projects/project_name/images/' created.
Put all images in this folder to be used as background images and make sure they are sortable alphabetically
Folder 'projects/project_name/output/' created.
Destination folder for the output video
Folder 'projects/project_name/temp/' created.
Used to hold the background music/audio combo file before creating video
```
- Next you will put mp3 files in the projects/project_name/audio folder that contain the main content (in my case narrative audio) make sure the names are alphabetically sortable
- Then you will add images to the projects/project_name/images folder -- again, ensure the names are alphabetically sortable. I used webp files, PNG's also work, look into the moviepy documentation for other image filetypes that would work.
- Add background music if you want, to the projects/project_name/background_music folder

As you can tell from the code, it's pretty simple so if there's anything you'd like to add or modify it won't take much, and please feel free to contribute if you have enhancements that you think the community would enjoy!

# Dependencies

* decorator
* imageio
* imageio-ffmpeg
* moviepy
* numpy
* pillow
* proglog
* pydub
* python-dotenv
* tqdm
