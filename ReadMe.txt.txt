Image Augmentation Code


This code is designed to expand the size of a training dataset by creating modified versions of images in the dataset.
This Script allows user to get desired number of output images from the input images in the folder.
The Images will randomly be augmented from the list of declared augmenters . 

The following image augmentation techniques are applied:

Horizontal Fliiping
Vertical Flipping
Affine-Rotates the images by random degree
Add Gaussian Noise
GaussianBlur
Hue and Saturation
Intensity Multiply
Crop to a percent of Image

NOTE --- The Range values for all the Augmenter functions can be changed 
         For more info on ImgAug Read Documentation
          https://imgaug.readthedocs.io/en/latest/



Prerequisites
Python 3.x
Numpy
OpenCV

Installations 
 
 pip install imgaug



Libraries 

-imgaug
-os
-random
-cv2


Getting Started 

- Create a folder 'images' in the same directory as your script and Get your images in the particular folder.
- Create folder 'images_aug' in the same directory for saving the augmented images.
- Run the augment.py script for the augmenations.


Usage (While file running)
-Enter the number of images per single images to be generated after augmentation.
-Enter Multiplying factor for intensity from range 0.1 to 2.0 .
 This helps to vary the intensity of image .
-Enter Cropping ratio for particular image from 0 to 1 in decimal .
 This will be the argument for crop augmenter to crop the image.

The augmented images will be stored in currentDir/images_aug folder.


Author 

Varad Rane (https://github.com/varadtechx)








