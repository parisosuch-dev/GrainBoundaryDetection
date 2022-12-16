from image_generation import extract_specimen_all, normalize
from tv_filter import generate_tv
from filters import contour_image
from PIL import Image as im


def GrainBoundaryDetection(file, weight=10, verbose=0):
    print("Starting Grain Detection...")

    phase, band, ipf_x, ipf_y, ipf_z, ipf_min, ipf_max = extract_specimen_all(file, verbose=verbose)

    ipf_x = generate_tv(ipf_x, "ipf_x", weight, verbose)
    ipf_y = generate_tv(ipf_y, "ipf_y", weight, verbose)
    ipf_z = generate_tv(ipf_z, "ipf_z", weight, verbose)
    ipf_min = generate_tv(ipf_min, "ipf_min", weight, verbose)
    ipf_max = generate_tv(ipf_max, "ipf_max", weight, verbose)
    band = generate_tv(band, "band", weight, verbose)

    threshold = 5

    ipf_x = ipf_x > threshold
    ipf_y = ipf_y > threshold
    ipf_z = ipf_z > threshold
    ipf_min = ipf_min > threshold
    ipf_max = ipf_max > threshold
    
    #threshold = 75
    #band = band > threshold

    if (verbose):
        
        #image = im.fromarray(band)
        #image = image.convert('RGB')
        #image.save("images/binary/band_image.png")

        image = im.fromarray(ipf_x)
        image = image.convert('RGB')
        image.save("images/binary/ipf_x_image.png")

        image = im.fromarray(ipf_y)
        image = image.convert('RGB')
        image.save("images/binary/ipf_y_image.png")

        image = im.fromarray(ipf_z)
        image = image.convert('RGB')
        image.save("images/binary/ipf_z_image.png")

        image = im.fromarray(ipf_min)
        image = image.convert('RGB')
        image.save("images/binary/ipf_min_image.png")

        image = im.fromarray(ipf_max)
        image = image.convert('RGB')
        image.save("images/binary/ipf_max_image.png")

    
    contour_image(ipf_x, "images/contour_ipf_x.png", overlay_img=True)
    contour_image(ipf_y, "images/contour_ipf_y.png", overlay_img=True)
    contour_image(ipf_z, "images/contour_ipf_z.png", overlay_img=True)
    contour_image(ipf_min, "images/contour_ipf_min.png", overlay_img=True)
    contour_image(ipf_max, "images/contour_ipf_max.png", overlay_img=True)
    #contour_image(band, "images/contour_band.png", overlay_img=True)
    contour_image(phase, "images/contour_phase.png", overlay_img=True)





specimen = open(r'/home/jdepriest/rock_final/data/11CSR01-p Specimen 1 Area 2 Montaged Data 1 Montaged Map Data-Ph + AE + BC + EDS (Al+Ca+Na+Fe+Si+K).csv')

GrainBoundaryDetection(specimen, weight=10, verbose=1)  # Edit this function. Weight changes TV filter weight, verbose saves images of each step in folders