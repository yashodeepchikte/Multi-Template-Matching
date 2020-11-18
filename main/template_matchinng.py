# -*- coding: utf-8 -*-
"""
@author: Yashodeep

@Roll number: 170003060
@Templates matching

@ This function should be given the image and list of tempaltes to be matched on that image
@ it will then return a list of probablity maps from multiple templates and with different template matching techniques
@ the return alue will be a list of tuples in this formatt
@ [ ......  ( probablity_map, template_widht, template_height )   .......   ] 
"""
import cv2 as cv
import numpy as np

from  NMS_2 import NMS

def template_matching(image, teplates, threshold=0.6):
    probablity_maps = []
    for template in teplates:
        w, h = template.shape[::-1]
            
        res = cv.matchTemplate(image,template,cv.TM_CCOEFF_NORMED)
        
        loc = np.where( res >= threshold)
        t = []
        for pt in zip(*loc[::-1]):
            t.append([pt[0], pt[1], res[pt[1]][ pt[0]], h, w])
        res =  NMS(t)        
        probablity_maps.append(res)
        
    return probablity_maps

