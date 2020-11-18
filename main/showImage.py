# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 21:22:50 2020

@author: yashodeep
@roll no 170003060


    
This function takes in the image and will display the image
process frozen till any key is not pressed on the keyboard
    

"""
import cv2 as cv

def show_image(window_name, img, threshold=0.7):   

    cv.imshow('image',img)
    cv.waitKey(0)
    cv.destroyAllWindows()
    return 0
