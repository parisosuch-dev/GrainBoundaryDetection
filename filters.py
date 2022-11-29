import skimage
import matplotlib.pyplot as plt
import numpy as np
import scipy.ndimage as ndi

def clean_image(file: str, save=False):
    """clean image through using the median to binary close and fill holes."""
    image_stack = skimage.io.imread(file, as_gray=True)
    footprint = skimage.morphology.disk(5)
    filtered = skimage.filters.median(image_stack, footprint=footprint)
    masked = filtered > skimage.filters.threshold_otsu(filtered)
    closed = skimage.morphology.binary_closing(masked, footprint=footprint)
    image_fill = ndi.binary_fill_holes(closed, footprint)
    if save:
        skimage.io.imsave(file[:-4]+"_filled_image.png", image_fill)
    return image_fill
def contour_image(file: str):
    # an (x, y, z) image where z is either 0 or 255 values for the binary image
    image_stack = skimage.io.imread(file)
    # get segmented image
    seg_img = clean_image(file)
    
    quad_contour_set = plt.contour([])

contour_image('images/phase_color_image.png')