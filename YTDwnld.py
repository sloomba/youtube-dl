from pytube import YouTube
import re

print 'YouTube Downloader - Sahil Loomba [using PyTube]\nFor downloading multiple videos from YouTube, in .mp4 format, in the highest available resolution.\n(Note that the default video filename is same as that on YouTube, and the videos are automatically stored in the current working directory.)'

def single_video (url):
	video_list = YouTube()
	print '>> Obtaining video details from', url, '...'
	try:
		video_list.url = url
		video = video_list.filter('mp4')[-1]
		video.download()
		print '>> Download of', video_list.filename, 'successful'
	except:
		print '>> Invalid video URL', url, 'or network is unreachable'

def playlist (html):
	try:
		html_file = open(html, 'r')
		html_data = html_file.readlines()
		html_file.close()
		url_list = []
		for line in html_data:
			if ('pl-video-title-link yt-uix-tile-link yt-uix-sessionlink  spf-link ' in line):
				href = re.findall('href\S+', line)
				url = href[0].split('"')
				url = url[1].split('&')
				url_list += [url[0]]
		print '>> Downloading', len(url_list), 'videos in the given playlist...'
		count = 1
		for url in url_list:
			single_video(url)
			print '>> Current Status: Done with', count, 'out of', len(url_list), 'videos'
			count += 1
	except: 
		print '>> Invalid YouTube playist webpage (.html file)', html, 'or network is unreachable'

def webpage (html):
	try:
		html_file = open(html, 'r')
		html_data = html_file.readlines()
		html_file.close()
		url_list = []
		for line in html_data:
			if ('yt-uix-sessionlink yt-uix-tile-link  spf-link  yt-ui-ellipsis yt-ui-ellipsis-2' in line):
				href = re.findall('href\S+', line)
				url = href[0].split('"')
				url = url[1].split('&')
				url_list += [url[0]]
		print '>> Downloading', len(url_list), 'videos on the given webpage...'
		count = 1
		for url in url_list:
			single_video(url)
			print '>> Current Status: Done with', count, 'out of', len(url_list), 'videos'
			count += 1
	except:
		print '>> Invalid YouTube webpage (.html file)', html, 'or network is unreachable'

sing_mult = raw_input('>> Enter \n\t1 to download a single video,\n\t2 to download a YouTube playlist,\n\t3 to download all videos on a YouTube webpage,\n\t0 to exit: ')
while (sing_mult != '0'):
	if (sing_mult == '1'):
		print '>> Single Video Downloader'
		url = raw_input('>> Enter video URL: ')
		single_video(url)
	elif (sing_mult == '2'):
		print '>> Playlist Videos Downloader'
		html = raw_input('>> Enter the .html filename of the YouTube playlist webpage: ')
		playlist(html)
	elif (sing_mult == '3'):
		print '>> Webpage Videos Downloader'
		html = raw_input('>> Enter the .html filename of the YouTube webpage: ')
		webpage(html)
	else:
		print '>> Invalid entry'
	sing_mult = raw_input('>> Enter \n\t1 to download a single video,\n\t2 to download a YouTube playlist,\n\t3 to download all videos on a YouTube webpage,\n\t0 to exit: ')
