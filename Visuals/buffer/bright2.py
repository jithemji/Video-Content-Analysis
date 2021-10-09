import sys
from PIL import Image


def calculate_brightness(image):
    greyscale_image = image.convert('L')
    histogram = greyscale_image.histogram()
    pixels = sum(histogram)
    brightness = scale = len(histogram)

    for index in range(0, scale):
        ratio = histogram[index] / pixels
        brightness += ratio * (-scale + index)

    return 1 if brightness == 255 else brightness / scale


if __name__ == '__main__':
    i=0
    
    
    image = Image.open("D:\\Project_Like_Prediction\\data\\frame"+str(i)+".jpg")
    
    print("%s\t%s" % (image, calculate_brightness(image)))