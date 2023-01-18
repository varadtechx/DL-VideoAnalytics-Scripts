import os
import cv2

folder_path = os.path.join(os.getcwd(), 'images') # Please put your folder name
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        
        with open(os.path.join(folder_path, filename), 'r') as file:
            contents = file.read()
            lines = contents.split('\n')
            
            for line in lines:
                split_line = line.split(' ')
                if split_line[0] == "2" :
                    label, x, y, width, height = line.strip().split(" ")
                    # x, y, width, height = int(x), int(y), int(width), int(height)
                    string=str(filename)
                    for i in range(0,len(string)) : 
                        if string[i]==".":
                            new_name=filename[0:i]
                    image_name = new_name + ".jpg" 
                    image_name=image_name.replace(' ','')
                    # print(image_name)
                    img = cv2.imread(image_name)
                    # img =
                    image_h, image_w = img.shape[:2]
                    w = width * image_w
                    h = height * image_h
                    x1 = ((2 * x * image_w) - w)/2
                    y1 = ((2 * y * image_h) - h)/2
                    x2 = x1 + w
                    y2 = y1 + h
                    
                    obj = img[x1:y1, x2:y2]
                    cv2.imwrite("images_aug/{}_{}.jpg".format(label,line), obj)


'''def yolo_to_pascal_voc(x, y, width, height ,  image_w, image_h):
    w = w * image_w
    h = h * image_h
    x1 = ((2 * x_center * image_w) - w)/2
    y1 = ((2 * y_center * image_h) - h)/2
    x2 = x1 + w
    y2 = y1 + h
    return [x1, y1, x2, y2]'''
