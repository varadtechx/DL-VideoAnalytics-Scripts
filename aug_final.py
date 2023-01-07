import os
import imgaug as ia
import imgaug.augmenters as iaa
import numpy as np
import imgaug as ia
import pybboxes as pbx
import imgaug.augmenters as iaa
from imgaug.augmentables.bbs import BoundingBox, BoundingBoxesOnImage



images = []
labels = []
classes =[]
#Datatset Reading
images_path = glob.glob("images/*.jpg")
labels_path = glob.glob("images/*.txt")

for img_path in images_path:
    img = cv2.imread(img_path)
    images.append(img)


for label_path in labels_path:
    labels_in_text=[]
    classes_in_text=[]
    text= open(label_path,"r") 
    for line in text:
        line=line.split()
        a=float(line[1])
        b=float(line[2])
        c=float(line[3])
        d=float(line[4])
        yolo_bbox = (a,b,c,d)
        height=1080
        width=1920
        labels_in_text.append(pbx.convert_bbox(yolo_bbox,from_type="yolo",to_type="voc",image_size=(width, height)))
        classes_in_text.append(line[0])
    text.close()
    labels.append(labels_in_text)
    classes.append(classes_in_text)




def get_augmentation_sequence():
    # Prompt the user to select the types of augmentation
    print("Select the types of augmentation to apply:")
    print("1. Flip horizontally")
    print("2. Flip vertically")
    print("3. Crop")
    print("4. Perspective transform")
    print("5. Elastic transform")
    print("6. Affine transform")
    print("7. Add Gaussian noise")
    print("8. Multiply intensity values")
    print("Enter the number of the augmentation(s), separated by a space:")
    augmentation_choices = input().split()
    # Create the augmentation sequence
    seq = iaa.Sequential()
    for choice in augmentation_choices:
        if choice == '1':
            seq.add(iaa.Fliplr(1.0))  # Flip horizontally with 100% probability
        elif choice == '2':
            seq.add(iaa.Flipud(1.0))  # Flip vertically with 100% probability
        elif choice == '3':
            seq.add(iaa.Crop(percent=(0, 0.1)))  # Crop up to 10% of the image
        elif choice == '4':
            seq.add(iaa.PerspectiveTransform(scale=(0.01, 0.1)))  # Apply perspective transform with a scale of 0.01 to 0.1
        elif choice == '5':
            seq.add(iaa.ElasticTransformation(alpha=(0, 10.0), sigma=0.25))  # Apply elastic transformation with alpha in the range 0 to 10 and sigma=0.25
        elif choice == '6':
            seq.add(iaa.Affine(rotate=45, translate_percent={"x": (-0.2, 0.2), "y": (-0.2, 0.2)}, scale=(0.8, 1.2)))  # Apply affine transformation with random rotation, translation, and scale
        elif choice == '7':
            seq.add(iaa.AdditiveGaussianNoise(scale=0.1*255))  # Add Gaussian noise with a scale of 0.1*255
        elif choice == '8':
            seq.add(iaa.Multiply((0.5, 1.5)))  # Multiply the intensity values by a scalar in the range 0.5 to 1.5
    
    return seq

aug = get_augmentation_sequence()


images_aug = []
labels_aug = []
for i in range(len(images)):
    bbs_list = []
    for j in range(len(labels[i])):
        bbs_list.append(BoundingBox(x1=labels[i][j][0], y1=labels[i][j][1], x2=labels[i][j][2], y2=labels[i][j][3]))
    bbs = BoundingBoxesOnImage(bbs_list, shape=images[i].shape)
    image_aug , bbs_aug = aug(image=images[i], bounding_boxes=bbs)
    images_aug.append(image_aug)
    labels_aug.append(bbs_aug)


for i in range(len(images_aug)):
    cv2.imwrite("images_aug/{}_aug.jpg".format(i), images_aug[i])
    f = open("images_aug/{}_aug.txt".format(i), "w")
    for j in range(len(labels_aug[i])):
        x1 = labels_aug[i][j].x1
        y1 = labels_aug[i][j].y1
        x2 = labels_aug[i][j].x2
        y2 = labels_aug[i][j].y2
        height=1080
        width=1920
        yolo_bbox = pbx.convert_bbox((x1,y1,x2,y2),from_type="voc",to_type="yolo",image_size=(width, height))
        f.write("{} {} {} {} {}\n".format(classes[i][j], "{:.6f}".format(yolo_bbox[0]), "{:.6f}".format(yolo_bbox[1]), "{:.6f}".format(yolo_bbox[2]), "{:.6f}".format(yolo_bbox[3])))


