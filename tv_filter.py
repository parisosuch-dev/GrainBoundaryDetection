from image_generation import *
import matplotlib.pyplot as plt

from skimage.restoration import (denoise_tv_chambolle, denoise_tv_bregman)


def generate_tv(image, filename, weight, verbose=0):
    image = normalize(image)    

    cham_image = denoise_tv_chambolle(image, weight=weight)

    if(verbose):
        cham_image = im.fromarray(cham_image)
        cham_image = cham_image.convert('RGB')
        cham_image.save("images/tv_images/tv_" + filename + "_" + str(weight) + ".png")


