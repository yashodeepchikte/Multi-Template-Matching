# -*- coding: utf-8 -*-
"""
@author: Yashoeep

@Roll number: 170003060
@Read Inputs

@ This function will read inputs from the inpus folder and store them properly 
@ in a dictionary which is also the return value


return valuedescription --> 

 {
  ...
  subject : {
      images: [ list of paths to images for this subject ]
      templates: [ list of paths to temppaltes for this subject ]
      results: [list of expected paths to the results of this subject ]
  }
  ....
 }



"""

import os
import cv2 as cv

def read_inputs():
    
    print("{0:=^50}".format(" Reading the Inputs "))
    
    # get the current working directory
    cwd = os.getcwd()
    cwd = cwd.replace("/", "\\")

    # ----------------------------------------setting the correct directory -------------------------------------------
    
    # if the current working directory is not the input images foolder then change it 
    temp_path = cwd.split("\\")
    
    # check if we are operating in the main folder
    if temp_path[-1] == "main":                
        
        inputs_root=os.path.join(cwd, "Inputs")
        subject_folder_names = [ item for item in os.listdir(inputs_root) if os.path.isdir(os.path.join(inputs_root, item)) ]
        #print (subject_folder_names)
        #print("There are {} subjects in the input".format( len(subject_folder_names) ))        
        
        subject_folder_paths = [os.path.join(inputs_root, item) for item in subject_folder_names]
        
        temp = {}
        
        for i, subject in enumerate(subject_folder_names):
            
            subject_folder_path = subject_folder_paths[i]
            
            subj_images_folder_path = os.path.join(subject_folder_path, "1_Images")
            subj_templates_folder_path = os.path.join(subject_folder_path, "2_Templates")
            subj_results_folder_path = os.path.join(subject_folder_path, "3_Processed_Images")
            
            
            subject_images_names = os.listdir(subj_images_folder_path)
            subject_template_names = os.listdir(subj_templates_folder_path)
            subject_results_names = ["processed_"+item for item in os.listdir(subj_images_folder_path)]
            
            subject_images_path = [os.path.join(subj_images_folder_path, item) for item in subject_images_names]
            subject_templates_path = [os.path.join(subj_templates_folder_path, item) for item in subject_template_names] 
            subject_results_path = [os.path.join(subj_results_folder_path, item) for item in subject_results_names]
            
            temp[subject] = {
                    "images": subject_images_path,
                    "templates": subject_templates_path,
                    "results": subject_results_path
                }
        return (temp, True)        
    else:
        print("{0:=^50}".format(" Reading Inputs --> Failed "))
        print("{0:=^50}".format(" Make sure you are in the same directory as the main.py file "))
        return ({}, False)
    
    

