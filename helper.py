import matplotlib.pyplot as plt
import numpy as np
from PIL import Image as im

def generatePlots(image_list, file_list):
    
    for i, image in enumerate(image_list):
        plt.plot(image)
        plt.savefig("plots/" + file_list[i] + "_plot.png")

def generateImages(image_list, file_list):

    for i, data in enumerate(image_list):
        array = np.array(data)
        array = normalize(array)
        image = im.fromarray(array)
        image = image.convert('RGB')
        image.save("images/" + file_list[i] + "_image.png")


def normalize(array):
    array = array.astype('float64')
    array = array[:,:-1]
    print(array.min(), array.max())
    array = array / array.max()
    array = array * 255
    print(array.min(), array.max())
    return array

def get_band_con(file):
    width = file.readline()
    height = file.readline()
    file.readline()

    width = width.split(",")
    width = int(width[1])

    height = height.split(",")
    height = int(height[1])

    band_con = np.zeros((width, height))

    for line in file:
        line = line.split(",")
        band_con[int(line[0])][int(line[1])] = line[2]

    return band_con


def get_phase_color(file):
    for i in range(11):
        file.readline()
    width = file.readline()
    height = file.readline()
    file.readline()

    width = width.split(",")
    width = int(width[1])
    height = height.split(",")
    height = int(height[1])

    phase_color = np.zeros((width, height))

    for line in file:
        line = line.split(",")
        phase_color[int(line[0])][int(line[1])] = int(line[2])

    return phase_color


def extract_specimen(file):
    file.readline()
    file.readline()

    width = 3523   # hard coded for data file
    height = 2028

    #phase = np.array((width, height))
    euler = np.zeros((width, height, 3))
    band = np.zeros((width, height))

    count = 0

    for line in file:
        line = line.split(",")
        #phase[int(line[1])][int(line[2])] = line[3]
        
        rgb = line[4].split()

        if (rgb[0] == "0" and rgb[1] == "255" and rgb[2] == "0"):
            euler[int(line[1])//10][int(line[2])//10][0] = 255
            euler[int(line[1])//10][int(line[2])//10][2] = 255
            euler[int(line[1])//10][int(line[2])//10][1] = 255
            count += 1
        else:
            euler[int(line[1])//10][int(line[2])//10][0] = int(rgb[0])
            euler[int(line[1])//10][int(line[2])//10][1] = int(rgb[1])
            euler[int(line[1])//10][int(line[2])//10][2] = int(rgb[2])            

        band[int(line[1])//10][int(line[2])//10] = line[5]
    
    image = im.fromarray(euler, mode="RGB")
    #image = image.convert('RGB')
    image.save("images/edit_euler_image.png")

    print(count)

    #image = im.fromarray(band)
    #image = image.convert('RGB')
    #image.save("images/s_band_image.png")
