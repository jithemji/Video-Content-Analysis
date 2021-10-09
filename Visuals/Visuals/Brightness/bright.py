    import os
    import glob

import cv2
import numpy as np
from PIL import Image
from PIL import ImageStat
import math

import matplotlib.pyplot as plt

def isbright(image, dim=10, thresh=0.5):
    # Resize image to 10x10
    image = cv2.resize(image, (dim, dim))
    # Convert color space to LAB format and extract L channel
    L, A, B = cv2.split(cv2.cvtColor(image, cv2.COLOR_BGR2LAB))
    # Normalize L channel by dividing all pixel values with maximum pixel value
    L = L/np.max(L)
    # Return True if mean is greater than thresh else False
    #return np.mean(L) > thresh
    return np.mean(L)
   # print(thresh)

def brightness( im_file ):
#    im = Image.open(im_file).convert('L')
#    stat = ImageStat.Stat(im)
#    return stat.rms[0]
    # im = Image.open(im_file)
    # stat = ImageStat.Stat(im)
    # r,g,b = stat.mean
    # return math.sqrt(0.241*(r**2) + 0.691*(g**2) + 0.068*(b**2))
    im = Image.open(im_file)
    stat = ImageStat.Stat(im)
    r,g,b = stat.rms
    return math.sqrt(0.241*(r**2) + 0.691*(g**2) + 0.068*(b**2))
    

# j=0
# i=0

# image = cv2.imread("D:\\Project_Like_Prediction\\data_"+str(j+1)+"\\frame"+str(i)+".jpg")
# print(brightness(image))


shots_brightness=[]
shots_brightness_f2=[]
df_brightness=[]
i=0
# image = cv2.imread("D:\\Track_ML\\data\\frame"+str(i)+".jpg")
# #print("D:\\Track_ML\\data\\frame"+str(i)+".jpg")
# print(isbright(image))
#shots_brightness=np.insert(isbright(image))


for j in range(5):
    path, dirs, files = next(os.walk("D:\Project_Like_Prediction\data_"+str(j+1)))
    file_count = len(files)

    i=0
    while(i<file_count):
        
        #image = cv2.imread("D:\\Project_Like_Prediction\\data_"+str(j+1)+"\\frame"+str(i)+".jpg")
        image="D:\\Project_Like_Prediction\\data_"+str(j+1)+"\\frame"+str(i)+".jpg"
        #temp=isbright(image)
        temp=brightness(image)
        #print(temp)
        shots_brightness=np.append(shots_brightness,brightness(image))
        i=i+1
    sum=0
    for i in range(file_count):
        sum+=shots_brightness[i]
    #print(sum)
    df_brightness=np.append(df_brightness,shots_brightness.mean())
    print("Avg Brightness"+str(j+1)+" : "+str(shots_brightness.mean()))
    
print(df_brightness)


