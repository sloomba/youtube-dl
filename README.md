YouTube Downloader - Sahil Loomba [using PyTube]

This is a python script which can download YouTube videos in their highest available resolution, in a .mp4 format. The script can download single videos, as well as multiple videos together (from either a YouTube playlist, or any YouTube webpage).

>> Requirements: Python must be installed on the machine; no restrictions on the operating system. The PyTube library must be installed as well.
(Note: Linux users can install PyTube by simply using "pip install pytube" from the terminal.)

>> Instructions:
	0. To run the script, simply use "python YTDwnld.py".
	1. To download a single video, you need only know the YouTube URL of the video.
	2. To download a YouTube playlist, open the "Playlists" tab of the YouTube channel, open the appropriate playlist by selecting "View full playlist", and save the webpage as a .html file in the working directory. Then, use the name of this .html file to download the entire playlist to your working directory.
	3. To download all videos present on a YouTube webpage, save the YouTube webpage as a .html file in the working directory. Then, use the name of this .html file to download all the videos of this webpage to your working directory.

(Note: All videos are saved in a .mp4 format, in their highest available resolution, with the filename same as the video name on YouTube, within the current working directory. A user familiar with Python and PyTube is free to tweak the source code to change these parameters suitably.)
