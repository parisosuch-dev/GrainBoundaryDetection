from image_generation import extract_specimen_all
from tv_filter import generate_tv


def GrainBoundaryDetection(file, weight=10, verbose=0):
    print("Starting Grain Detection...")

    phase, band, ipf_x, ipf_y, ipf_z, ipf_min, ipf_max = extract_specimen_all(file, verbose=verbose)

    ipf_x = generate_tv(ipf_x, "ipf_x", weight, verbose)
    ipf_y = generate_tv(ipf_y, "ipf_y", weight, verbose)
    ipf_z = generate_tv(ipf_z, "ipf_z", weight, verbose)
    ipf_min = generate_tv(ipf_min, "ipf_min", weight, verbose)
    ipf_max = generate_tv(ipf_max, "ipf_max", weight, verbose)

    # TODO: Paris Functions here

    # TODO: Phase and ipf comparison




specimen = open(r'/home/jdepriest/rock_final/data/11CSR01-p Specimen 1 Area 2 Montaged Data 1 Montaged Map Data-Ph + AE + BC + EDS (Al+Ca+Na+Fe+Si+K).csv')

GrainBoundaryDetection(specimen, weight=10, verbose=0)  # Edit this function. Weight changes TV filter weight, verbose saves images of each step in folders