"""
@author: Yashodeep
@Roll number: 170003060

@Input: 
Simply run this file 

@Output: 
All the processed images will be saved in subject folders the inputs folder itself 
"""
from read_inputs import read_inputs 
import cv2 as cv
from showImage import show_image
from template_matchinng import template_matching
from  NMS_2 import NMS
from create_template import create_template

if __name__ == "__main__":
    
    (inputs, success) = read_inputs()
    num_subjects = len(inputs)
    if success:      
        print("Starting processing")
        for a, subject in enumerate(inputs):
            # print("Processing ", subject,"|| overall Progress -->  {0: >3} % done".format(((a+1)/num_subjects)*100))
            images = inputs[subject]["images"]
            results = inputs[subject]["results"]
            templates = inputs[subject]["templates"]
            templates = [cv.imread(template_path, 0) for template_path in templates]
            T = []
            for template in templates:
                T += create_template(template)
             
            for i, image_path in enumerate(images):
                print("Processing ", subject,"||  Progress -->  {0: >3} % done".format(((i+1)/len(images))*100))

                image = cv.imread(i age_path)
                img_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
                probablity_maps = template_matching(img_gray, templates, threshold=0.7)
                points = []
                for temp_maps in probablity_maps:
                    for point in temp_maps:
                        points.append(point)
                points = NMS(points)
                for pt in points:
                    [xi, yi, ci, hi, wi] = pt
                    cv.rectangle(image, (xi, yi), (xi + wi, yi + hi), (0,0,255), 1)                
                cv.imwrite(results[i], image )
        print("The program execution is completed")
        print("Please check the results stored in the processed images folder for each subject inside the inputs folder")
    else:
        print("Program failed to read the inputs")
        
        
        
        
        
        
        
        
        



        

