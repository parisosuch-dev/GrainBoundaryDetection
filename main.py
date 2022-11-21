import pandas as pd
from PIL import Image as im
import matplotlib.pyplot as plt
import numpy as np
from helper import *


al_data = pd.read_csv(r'/home/jdepriest/rock_final/data/Al Kα1.csv')
#band_contrast = pd.read_csv(r'/home/jdepriest/rock_final/data/Band Contrast 223.csv', skiprows=2)
ca_data = pd.read_csv(r'/home/jdepriest/rock_final/data/Ca Kα1.csv')
fe_data = pd.read_csv(r'/home/jdepriest/rock_final/data/Fe Kα1.csv')
ipf_x_color = pd.read_csv(r'/home/jdepriest/rock_final/data/IPF X Color 223.csv')
ipf_y_color = pd.read_csv(r'/home/jdepriest/rock_final/data/IPF Y Color 223.csv')
ipf_z_color = pd.read_csv(r'/home/jdepriest/rock_final/data/IPF Z Color 223.csv')
k_data = pd.read_csv(r'/home/jdepriest/rock_final/data/K Kα1.csv')
na_data = pd.read_csv(r'/home/jdepriest/rock_final/data/Na Kα1,2.csv')
#phase_color = pd.read_csv(r'/home/jdepriest/rock_final/data/Phase Color 223.csv')
si_data = pd.read_csv(r'/home/jdepriest/rock_final/data/Si Kα1.csv')

specimen = open(r'/home/jdepriest/rock_final/data/11CSR01-p Specimen 1 Area 2 Montaged Data 1 Montaged Map Data-Ph + AE + BC + EDS (Al+Ca+Na+Fe+Si+K).csv')

#extract_specimen(specimen)
get_phase_color(specimen)

#specimen = np.array(specimen)

#print(specimen.shape, specimen.min(), specimen.max())

#f = open('/home/jdepriest/rock_final/data/Phase Color 223.csv')
#phase_color = get_phase_color(f)

#f = open('/home/jdepriest/rock_final/data/Band Contrast 223 Panda.csv')
#band_con = get_band_con(f)

#print(phase_color.shape, phase_color.min(), phase_color.max())
#generateImages([[phase_color]], ["phase_color"])


#ipf_image = np.zeros((ipf_x_color.shape[0], ipf_x_color.shape[1], 3))

#print(ipf_image.shape)

#ipf_image[:,:,0] = ipf_x_color
#ipf_image[:,:,1] = ipf_y_color
#ipf_image[:,:,2] = ipf_z_color

#print(ipf_x_color.shape)

#ipf_x_color = np.array(ipf_x_color)

#ipf_x_color = ipf_x_color[:,:-1]

#print(ipf_x_color.min(), ipf_x_color.max(), sep="\n")
#print(ipf_x_color)

#all_data = [si_data, na_data, al_data, ca_data, fe_data, ipf_x_color, ipf_y_color, ipf_z_color, k_data]
#all_files = ["si", "na", "al", "ca", "fe", "ipf_x", "ipf_y", "ipf_z", "k"]

#generateImages(all_data, all_files)


#generateImages([al_data], ["al_image_norm"])

#generatePlots(all_data, all_files)