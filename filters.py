import skimage
import matplotlib.pyplot as plt
import numpy as np
import scipy.ndimage as ndi

def remove_gaussian_noise(file: str):
    arr = np.asarray(skimage.img_as_float(skimage.io.imread(file)))
    avg = np.mean(arr,0).astype('uint8')
    skimage.io.imsave(file[:-4]+"_noise_removed.png", avg)

remove_gaussian_noise("images/phase_color_image.png")