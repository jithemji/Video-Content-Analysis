# Importing all necessary libraries
import cv2
import os
import time
import vlc
import pafy
import youtube_dl

# Read the video from specified path
#cam = cv2.VideoCapture('https://www.youtube.com/watch?v=EboTIyWDuCo&list=PLLy_2iUCG87CNafffzNZPVa9rW-QmOmEv')
video_url = 'https://www.youtube.com/watch?v=t8JRidxZCXU'

ydl_opts = {}

# create youtube-dl object
ydl = youtube_dl.YoutubeDL(ydl_opts)

# set video url, extract video information
info_dict = ydl.extract_info(video_url, download=False)
#cam = pafy.new('https://www.youtube.com/watch?v=EboTIyWDuCo&list=PLLy_2iUCG87CNafffzNZPVa9rW-QmOmEv')
formats = info_dict.get('formats',None)


for f in formats:

# I want the lowest resolution, so I set resolution as 144p
    if f.get('format_note',None) == '360p':

        #get the video url
        url = f.get('url',None)

        # open url with opencv
        cap = cv2.VideoCapture(url)

        # check if url was opened
        if not cap.isOpened():
            print('video not opened')
            exit(-1)

cam=cap

frames = cam.get(cv2.CAP_PROP_FRAME_COUNT)
fps = int(cam.get(cv2.CAP_PROP_FPS))
  
# calculate dusration of the video
seconds = int(frames / fps)

try:

    # creating a folder named data
    if not os.path.exists('data'):
        os.makedirs('data')

    # if not created then raise error
except OSError:
    print('Error: Creating directory of data')

# frame
currentframe = 0
print(seconds)
temp=seconds/10
print(temp)
i=0
count=0

while (True):
    time.sleep(5) # take schreenshot every 5 seconds
    # reading from frame
    
    ret, frame = cam.read()
    #i=i+temp

    if ret:
        # if video is still left continue creating images
        name = './data/frame' + str(currentframe) + '.jpg'
        print('Creating...' + name)

        # writing the extracted images
        cv2.imwrite(name, frame)
        count += 30*temp # i.e. at 30 fps, this advances one second
        cam.set(1, count)

        # increasing counter so that it will
        # show how many frames are created
        currentframe += 1
    else:
        break

# Release all space and windows once done
cam.release()
cv2.destroyAllWindows()