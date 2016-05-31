import os, sys
import subprocess
from scipy import misc
import numpy as np

def create_frames(video_path):
	subprocess.call('ffmpeg -i '+video_path+ ' frames/image-%d.jpg', shell=True)

def read_image(image_path):
	arr = misc.imread(image_path)
	print(arr[8,20])

def create_frames_usingcv(path):
	vidcap = cv2.VideoCapture(path)
	success,image = vidcap.read()
	count = 0;
	while success:
	  success,image = vidcap.read()
	  cv2.imwrite("frames/frame%d.jpg" % count, image)     # save frame as JPEG file
	  if cv2.waitKey(10) == 27:                     # exit if Escape is hit
	      break
	  count += 1
	
def create_frames_folder(folder_path):
	for content in os.listdir(folder_path):
		create_frames(folder_path+'/'+content)
		for content_image in os.listdir("frames"):
			read_image("frames/"+content_image)


if __name__ == "__main__":
    create_frames('8232768892322701272.mp4')
    read_image('frames/image-1.jpg')
    create_frames_folder("frames")
