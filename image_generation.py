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

def normalize_float(array):
    array = array.astype('float64')
    array = array / array.max()
    return array

def normalize(array):
    array = array.astype('float64')
    array = array[:,:-1]
    array = array / array.max()
    array = array * 255
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




def get_phase_color(file, save_image=True):
    file.readline()
    file.readline()

    width = 3523   # hard coded for data file
    height = 2028

    #euler_phase = np.zeros((height, width, 3))      # This one to generate normal image. Next to generate white image.
    euler_phase = np.full((height, width, 3), 255)

    count = 0

    for line in file:
        line = line.split(",")
        
        rgb = line[4].split()

        y = int(line[1])//10
        x = int(line[2])//10

        rgb = np.array(rgb, "int")

        if (int(line[3]) == 1):
            euler_phase[x,y,:] = rgb
        else:
            euler_phase[x,y,:] = [255,255,255]

    if(save_image):
        image = im.fromarray(euler_phase, mode="RGB")
        #image = image.convert("RGB")
        image.save("images/euler_phase_white_all.png")

    return euler_phase


def get_element_images(file):
    file.readline()
    file.readline()

    width = 3523
    height = 2028

    al_image = np.zeros((height, width))
    ca_image = np.zeros((height, width))
    na_image = np.zeros((height, width))
    fe_image = np.zeros((height, width))
    si_image = np.zeros((height, width))
    k_image = np.zeros((height, width))
    

    for line in file:
        line = line.split(",")

        elements = line[6].split()

        y = int(line[1])//10
        x = int(line[2])//10

        al_image[x,y] = float(elements[0])
        ca_image[x,y] = float(elements[1])
        na_image[x,y] = float(elements[2])
        fe_image[x,y] = float(elements[3])
        si_image[x,y] = float(elements[4])
        k_image[x,y] = float(elements[5])

    image_list = [al_image, ca_image, na_image, fe_image, si_image, k_image]
    file_list = ["al", "ca", "na", "fe", "si", "k"]

    for i, data in enumerate(image_list):
        array = np.array(data)
        array = normalize(array)
        image = im.fromarray(array)
        image = image.convert('RGB')
        image.save("images/phase_" + file_list[i] + ".png")

    average_images(image_list)


def average_images(images):
    sum_image = np.zeros((images[0].shape[0], images[0].shape[1]))

    for image in images:
        sum_image += image
    
    avg_img = sum_image / len(images)

    generateImages([avg_img], ["avg_element"])
    

def subset_of_euler(file):
    file.readline()
    file.readline()

    width = 300
    height = 300

    euler = np.zeros((height, width, 3))

    for n in range(1000):
        file.readline()

    for i in range(300):
        for j in range(300):
            line = file.readline()
            line = line.split(",")

            rgb = line[4].split()

            y = int(line[1])//10
            x = int(line[2])//10

            euler[i,j,:] = rgb

    euler = normalize(euler)
    image = im.fromarray(euler, "RGB")
    image = image.convert('RGB')
    image.save("images/subset_euler_image.png")

        


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



def extract_specimen_all(file):
    file.readline()
    file.readline()

    width = 3523   # hard coded for data file
    height = 2028

    phase = np.zeros((height, width))
    euler = np.zeros((height, width, 3))
    band = np.zeros((height, width))
    al_image = np.zeros((height, width))

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

    return [phase, band]

    #generateImages([phase], ["phase_color"])

    #image = im.fromarray(euler, mode="RGB")
    #image = image.convert('RGB')
    #image.save("images/edit_euler_image.png")

    #print(count)

    #image = im.fromarray(band)
    #image = image.convert('RGB')
    #image.save("images/s_band_image.png")

def get_filter_data(file):
    file.readline()
    file.readline()

    width = 3523   # hard coded for data file
    height = 2028

    phase = np.zeros((height, width))
    band = np.zeros((height, width))

    for line in file:
        line = line.split(",")
        
        rgb = line[4].split()

        y = int(line[1])//10
        x = int(line[2])//10

        phase[x][y] = int(line[3])

        band[x][y] = line[5]


    return (phase, band)