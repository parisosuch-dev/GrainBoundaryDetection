from image_generation import *
import pandas as pd
import matplotlib.pyplot as plt

from skimage.restoration import (denoise_tv_chambolle, denoise_tv_bregman)


def generate_tv(image, filename):
    image = normalize(image)    

    for weight in [.1,.5,1,5,10000]:
        breg_image = denoise_tv_bregman(image, weight=weight)
        #cham_image = denoise_tv_chambolle(image, weight=weight)

        math_breg = image - breg_image
        #math_cham = image - cham_image

        math_breg = np.absolute(math_breg)
        #math_cham = np.absolute(cham_image)

        breg_image = im.fromarray(breg_image)
        breg_image = breg_image.convert('RGB')
        breg_image.save("images/tv_images/" + filename + "_breg_" + str(weight) + ".png")

        #cham_image = im.fromarray(cham_image)
        #cham_image = cham_image.convert('RGB')
        #cham_image.save("images/tv_images/" + filename + "_cham_" + str(weight) + ".png")

        math_breg = im.fromarray(math_breg)
        math_breg = math_breg.convert('RGB')
        math_breg.save("images/tv_images/" + filename + "_breg_" + str(weight) + "_math.png")

        #math_cham = im.fromarray(math_cham)
        #math_cham = math_cham.convert('RGB')
        #math_cham.save("images/tv_images/" + filename + "_cham_" + str(weight) + "_math.png")

def main():
    specimen = open(r'/home/jdepriest/rock_final/data/11CSR01-p Specimen 1 Area 2 Montaged Data 1 Montaged Map Data-Ph + AE + BC + EDS (Al+Ca+Na+Fe+Si+K).csv')
    ipf_x_color = pd.read_csv(r'/home/jdepriest/rock_final/data/IPF X Color 223.csv')
    ipf_y_color = pd.read_csv(r'/home/jdepriest/rock_final/data/IPF Y Color 223.csv')
    ipf_z_color = pd.read_csv(r'/home/jdepriest/rock_final/data/IPF Z Color 223.csv')
    ipf_x_color = np.array(ipf_x_color)
    ipf_y_color = np.array(ipf_y_color)
    ipf_z_color = np.array(ipf_z_color)
    ipf_x_color = np.absolute(ipf_x_color)
    ipf_y_color = np.absolute(ipf_y_color)
    ipf_z_color = np.absolute(ipf_z_color)

    binary_phase, band_constrast = get_filter_data(specimen)

    file_list = [ipf_x_color, ipf_y_color, ipf_z_color, binary_phase, band_constrast]
    filenames = ["ipf_x", "ipf_y", "ipf_z", "phase", "band"]
    for i in range(len(file_list)):
        generate_tv(file_list[i], filenames[i])

    #ipf_x_color = normalize(ipf_x_color)
    #ipf_y_color = normalize(ipf_y_color)
    #ipf_z_color = normalize(ipf_z_color)

    #tv_phase = denoise_tv_chambolle(binary_phase, weight=3, channel_axis=-1)
    #tv_ipf_x = denoise_tv_chambolle(ipf_x_color, weight=50, channel_axis=-1)
    #tv_ipf_y = denoise_tv_chambolle(ipf_y_color, weight=1, channel_axis=-1)
    #tv_ipf_z = denoise_tv_chambolle(ipf_z_color, weight=1, channel_axis=-1)
    #tv_band = denoise_tv_chambolle(band_constrast, weight=0.1, channel_axis=-1)


main()


