import skimage
from skimage.color import label2rgb
import matplotlib.pyplot as plt
import numpy as np
import scipy.ndimage as ndi

def clean_image(arr) -> np.ndarray:
    """clean image through using the median to binary close and fill holes."""
    footprint = skimage.morphology.disk(5)
    #filtered = skimage.filters.median(image_stack, footprint=footprint)
    masked = arr > skimage.filters.threshold_otsu(arr)
    influence_region = np.ones((5,5))
    step1 = skimage.morphology.binary_dilation(masked, footprint=influence_region)
    step2 = skimage.morphology.binary_erosion(step1, footprint=influence_region)
    step3 = skimage.morphology.binary_erosion(step2, footprint=influence_region)
    step4 = skimage.morphology.binary_dilation(step3, footprint=influence_region)
    image_fill = ndi.binary_fill_holes(step4, skimage.morphology.disk(5))
    #closed = skimage.morphology.binary_closing(masked, footprint=footprint)
    #image_fill = ndi.binary_fill_holes(closed, footprint)
    return image_fill

def contour_image(arr, save_path=None, overlay_img=False):
    # an (x, y, z) image where z is either 0 or 255 values for the binary image
    cleaned_img = clean_image(arr)
    cleaned_img = ndi.binary_fill_holes(cleaned_img)
    labeled_grains, _ = ndi.label(cleaned_img)
    img_label_overlay = label2rgb(labeled_grains, image=arr, bg_label=0)
    if overlay_img:
        fig, axes = plt.subplots(1,2, figsize=(10,10), sharey=True)
        axes[0].imshow(arr, cmap='gray')
        axes[0].contour(cleaned_img, [0.5], linewidths=0.3, colors='r')
        axes[1].imshow(img_label_overlay)
        for a in axes:
            a.axis('off')
    else:
        plt.figure()
        plt.imshow(arr, cmap='gray')
        plt.contour(cleaned_img, [0.5], linewidths=0.3, colors='r')
    plt.tight_layout()
    if save_path is None:
        plt.savefig('images/contour.png', dpi=300)
    else:
        plt.savefig(save_path, dpi=300)

