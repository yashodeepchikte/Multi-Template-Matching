# -*- coding: utf-8 -*-
"""
@author: Yashoeep

@Roll number: 170003060
@NMS --> non maxima supression and also overlapping recrangles will be removed

@ This function will take a list of points as inputs 
@ the format of these points --> [ [xcoor, y_coor, confidence, height, width] ]
"""


def NMS(B, threshold=0.6):
    # B ---> [ ....[xcoor, y_coor, confidence, height, width] ......] 
    B = sorted(B, key = lambda a: a[2], reverse=True)
    i = 0
    while i < len(B):
        j = i + 1
        while j < len(B):
            (xi, yi, ci, hi, wi) = B[i]
            (xj, yj, cj, hj, wj) = B[j]
            
            if (min(xi+wi, xj+wj) - max(xi, xj)) > 0 and (min(yi+hi, yj+hj) - max(yi, yj)) >0:
                over_lapping_area = (min(xi+wi, xj+wj) - max(xi, xj) )*(min(yi+hi, yj+hj) - max(yi, yj))
                total_area = hi*wi + hj*wj - over_lapping_area
                
                if over_lapping_area/total_area > threshold:
                    B.remove(B[j])
                    continue
                else:
                    j += 1
            else:
                j += 1
        i += 1
    
    return B


