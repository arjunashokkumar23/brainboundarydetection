import cv2
import numpy as np
from collections import Counter


def extractSlicesandBoundaries(final_names):
    DIR_PATH = './testPatient/'
    OUTPUT_PATH = './'
    for f in final_names:

        image = cv2.imread(DIR_PATH+'/'+f)
        f = f[:len(f)-4]
        gray_scale = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

        thresh = cv2.threshold(gray_scale,0,255,cv2.THRESH_BINARY)[1]

        contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        contours = contours[0] if len(contours) == 2 else contours[1]
        x_list = list()
        y_list = list()
        for c in contours:
            x,y,w,h = cv2.boundingRect(c)
            if w==4 and h==5:
                x_list.append(x)
                y_list.append(y)

        x_coord = Counter(x_list)
        y_coord = Counter(y_list)
        final_x = [x for x in x_coord.keys() if x_coord[x] > 1]
        final_x.sort()
        final_y = [y for y in y_coord.keys() if y_coord[y] > 1]
        final_y.sort()
        final_width = final_x[1] - final_x[0]
        final_height = final_y[1] - final_y[0]
        start_y = final_y[0] - final_height
        final_y.append(start_y)
        final_y.sort()

        name_idx = 1
        
        for y in final_y:
            for x in final_x:
                new_image = image[y+5:y+final_height, x+4:x+final_width]
                new_grayscale = cv2.cvtColor(new_image,cv2.COLOR_BGR2GRAY)
                new_thresh = cv2.threshold(new_grayscale,0,255,cv2.THRESH_BINARY)[1]
                if cv2.countNonZero(new_grayscale) != 0:
                    
                    cv2.imwrite(OUTPUT_PATH+'Slices/'+f+'/'+str(name_idx)+".png", new_image)
                    contours1 = cv2.findContours(new_thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                    contours1 = contours1[0] if len(contours1) == 2 else contours1[1]
                    boundary_image = new_image.copy()
                    cv2.drawContours(boundary_image, contours1, -1, (255,0,0), 2)
                    
                    cv2.imwrite(OUTPUT_PATH+'Boundaries/'+f+'/'+str(name_idx)+".png", boundary_image)
                    name_idx +=1
