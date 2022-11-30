import skimage
from skimage.feature import canny
from skimage.color import label2rgb
import matplotlib.pyplot as plt
import numpy as np
import scipy.ndimage as ndi

def clean_image(file: str, save=False) -> np.ndarray:
    """clean image through using the median to binary close and fill holes."""
    image_stack = skimage.io.imread(file, as_gray=True)
    footprint = skimage.morphology.disk(2)
    filtered = skimage.filters.median(image_stack, footprint=footprint)
    masked = filtered > skimage.filters.threshold_otsu(filtered)
    closed = skimage.morphology.binary_closing(masked, footprint=footprint)
    image_fill = ndi.binary_fill_holes(closed, footprint)
    if save:
        skimage.io.imsave(file[:-4]+"_filled_image_3.png", image_fill)
    return image_fill

def opening_process(img: np.ndarray, footprint_size=2) -> np.ndarray:
    """Remove noise in image through erosion process->dilation process"""
    # erode the img using a square structuring element
    footprint = skimage.morphology.square(footprint_size)
    eroded_img = skimage.morphology.binary_erosion(img, footprint=footprint)
    dilated_img = skimage.morphology.binary_dilation(eroded_img, footprint=footprint)
    return dilated_img
def closing_process(img: np.ndarray, footprint_size=2) -> np.ndarray:
    """Close holes in image through dilation->erosion"""
    footprint = skimage.morphology.square(footprint_size)
    dilated_img = skimage.morphology.binary_dilation(img, footprint=footprint)
    eroded_img = skimage.morphology.binary_erosion(dilated_img, footprint=footprint)
    return eroded_img



def contour_image(file: str, save_path=None):
    # get og image
    img = skimage.io.imread(file)
    # an (x, y, z) image where z is either 0 or 255 values for the binary image
    cleaned_img = clean_image(file)
    cleaned_img = ndi.binary_fill_holes(cleaned_img)
    labeled_grains, _ = ndi.label(cleaned_img)
    img_label_overlay = label2rgb(labeled_grains, image=img, bg_label=0)
    
    fig, axes = plt.subplots(1,2, figsize=(8,3), sharey=True)
    axes[0].imshow(img)
    axes[0].contour(cleaned_img, [0.5], linewidths=0.5, colors='r')
    axes[1].imshow(img_label_overlay)

    for a in axes:
        a.axis('off')
    plt.tight_layout()
    plt.savefig('images/overlay.png')


contour_image('images/phase_color_image.png')