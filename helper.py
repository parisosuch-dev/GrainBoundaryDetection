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
    file.readline()
    file.readline()

    width = 3523   # hard coded for data file
    height = 2028

    euler_phase = np.zeros((height, width, 3))      # This one to generate normal image. Next to generate white image.
    #euler_phase = np.full((height, width, 3), 255)

    count = 0

    for line in file:
        line = line.split(",")
        
        rgb = line[4].split()

        y = int(line[1])//10
        x = int(line[2])//10

        rgb = np.array(rgb, "int")

        if (int(line[3]) == 1):
            euler_phase[x,y,:] = rgb
            count += 1


    image = im.fromarray(euler_phase, mode="RGB")
    #image = image.convert("RGB")
    image.save("images/euler_phase_white.png")

    print(count)


    


def extract_specimen(file):
    file.readline()
    file.readline()

    width = 3523   # hard coded for data file
    height = 2028

    phase = np.zeros((height, width))
    euler = np.zeros((height, width, 3))
    band = np.zeros((height, width))
    al_image = np.zeros((height, width))

    count = 0

    for line in file:
        line = line.split(",")
        
        rgb = line[4].split()

        y = int(line[1])//10
        x = int(line[2])//10

        element = line[6].split()

        phase[x][y] = int(line[3])

        al_image[x][y] = float(element[0])

        if (rgb[0] == "0" and rgb[1] == "255" and rgb[2] == "0"):
            euler[x][y][0] = 255
            euler[x][y][2] = 255
            euler[x][y][1] = 255
            #count += 1
        else:
            euler[x][y][0] = int(rgb[0])
            euler[x][y][1] = int(rgb[1])
            euler[x][y][2] = int(rgb[2])            

        band[x][y] = line[5]
    
    generateImages([al_image], "phase_al")

    #generateImages([phase], ["phase_color"])

    #image = im.fromarray(euler, mode="RGB")
    #image = image.convert('RGB')
    #image.save("images/edit_euler_image.png")

    #print(count)

    #image = im.fromarray(band)
    #image = image.convert('RGB')
    #image.save("images/s_band_image.png")
