# GrainBoundaryDetection

To run the code, you must have the specimen csv file in a folder called "data/". 
- Feel free to change the parameters in the GrainBoundaryDetection() method. 
- The specimen argument is the csv file opened. 
- The weight is the weight for the threshold (default is 10)
- Verbose is by default set to 1, which is a boolean for whether or not the filtered images are saved in a folder as well. 

The key files in this project is:
- main.py
- image_generation.py
- tv_filter.py
- filters.py

## image_generation.py

extract_specimen_all(file, verbose=verbose)
- returns the images in a numpy array representation, crucial for getting the various types of images
- creates phase, band, ipf_x, ipf_y, ipf_z, ipf_min, and ipf_max arrays

## tv_filter.py

generate_tv(image, filename, weight, verbose=0)
- uses a total variation filter on the image being passed

## filters.py

clean_image(arr)
- does a closing process morphological filter on the array being passed

contour_image(arr, save_path=None, overlay_img=False)
- find the edges to the array being passed