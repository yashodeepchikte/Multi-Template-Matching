"""
@author: Kailash
@Roll number: 170003019

@Input: 
a image as input

@Output: 
list of different templates.
"""
import numpy as np
import cv2
from matplotlib import pyplot as plt


def create_template(img):

	# read image as greyscale  
	img = cv2.imread(img,1);


	#tempt1 = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE) 
	t1 = img
	t2 = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
	t3 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
	t4 = cv2.rotate(img, cv2.ROTATE_180)

	t11 = cv2.flip(t1, 1)
	t22 = cv2.flip(t2, 0)
	t33 = cv2.flip(t3, 0)
	t44 = cv2.flip(t4, 1)

	t = [t1, t2, t3, t4, t11, t22, t33, t44]
	return t

'''img = 'images.jpg'
tt = create_template(img)
plt.imshow(tt[1])
plt.show()'''