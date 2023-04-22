# Brain Boundary Detection

This project works with the fMRI images of the Human brain.

- It takes the fMRI images as input.
- Processes the image using OpenCV
- Slices the single images into multiple small images consisting of each brain slice in a different image.
- This marks the first step of the project.

- Later, these slices are imported back.
- Boundaries of the brain images in each of these image slices are obtained using Contour detection.
- These boundaries are then drawn onto the images to clearly demarcate the edges of the human brain.

## Steps to execute the code

- The input images are kept in a folder called 'testPatient'
- The test.py file acts as a helper function to maintain the folder paths and creation of the sub folders namely, Slices and Boundaries.

- The brainextraction.py file fetches the images, slices it and then draws the brain boundaries on each brain contour.
- The sliced images are stored in the Slices folder
- The slices images with the brain boundaries are stored in the Boundaries folder.