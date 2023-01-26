import imgaug as ia
import imgaug.augmenters as iaa
import random
import os
import cv2



num_augmented_images = int(input("Enter the number of augmented images per original image: "))
mul=float(input("Enter Multiplying factor for intensity from range 0.1 to 2.0"))
c=float(input("Enter Cropping ratio for particular image from 0 to 1 in decimal"))

augmentations = [
    iaa.Fliplr(1), #Mirror Flipping
    iaa.Flipud(1), # vertically flip images
    iaa.Affine(rotate=(-45, 45)), # rotate the images by a random degree between -45 and 45
    iaa.AdditiveGaussianNoise(scale=(0, 0.05*255)), # add random noise to the images
    iaa.GaussianBlur(sigma=(0, 1.0)), # blur the images with a random sigma between 0 and 1
    iaa.AddToHueAndSaturation(value=(-10, 10)), # change the hue and saturation of the images by a random value between -10 and 10
    iaa.Multiply((mul)), #Intensity value from user input
    iaa.Crop(percent=(0,c))
]

# For input and output folders
input_folder = os.path.join(os.getcwd(), 'images')
output_folder = os.path.join(os.getcwd(), 'images_aug')

# Iterate through the images in the input folder
for filename in os.listdir(input_folder):
    
    if filename.endswith(".jpg") or filename.endswith(".png"):
        
        image = cv2.imread(os.path.join(input_folder, filename))

        # Augment the image num_augmented_images times
        for i in range(num_augmented_images):
            # Apply a random augmentation
            random_augmentation = random.choice(augmentations)
            augmented_image = random_augmentation.augment_image(image)

            # Saving the augmented image
            cv2.imwrite(os.path.join(output_folder, f"{filename}_{i}.jpg"), augmented_image)

print("Augmentation completed!")
