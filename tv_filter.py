from image_generation import *
from skimage.restoration import denoise_tv_chambolle


def generate_tv(image, filename, weight, verbose=0):
    image = normalize(image)    

    cham_image = denoise_tv_chambolle(image, weight=weight)

    if(verbose):
        img = im.fromarray(cham_image)
        img = img.convert('RGB')
        img.save("images/tv_images/tv_" + filename + "_" + str(weight) + ".png")

    return cham_image
