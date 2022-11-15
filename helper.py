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