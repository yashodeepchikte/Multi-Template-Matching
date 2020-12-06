# Multi-template matching ![visitors](https://visitor-badge.laobi.icu/badge?page_id=yashodeepchikte.Multi-Template-Matching)
A versatile  pipeline for object-localization in microscopy images using Template Matching

# Overview
The localization of objects of interest is a key initial step in most image analysis workflows. For biomedical image data, classical image-segmentation methods like thresholding or edge detection are typically used. While those methods perform well for labeled objects, they are reaching a limit when samples are poorly contrasted with the background, or when only parts of larger structures should be detected.
We propose a new straightforward and generic approach for object-localization by template matching conditions.

![overview image 1](https://github.com/yashodeepchikte/Multi-Template-Matching/blob/master/main/Assets/images/1.JPG)
![overview image 2](https://github.com/yashodeepchikte/Multi-Template-Matching/blob/master/main/Assets/images/2.JPG)

# Description
Generally, in a microscopic image, the main subject of interest is located in a very small field of view and is randomly positioned in the image. Our aim here is to develop a generalized way to localize the subject or subjects to zero down on that area in the image containing the subject/subjects. And for doing so, studying different template matching techniques and trying to mitigate the problems created by differences in size and noise in the image to get the best results most of the time. <br/>
We wish to define a workflow so the user can easily and effectively use this tool for localising subjects in their images as per the templates that the user will provide.


# Workflow
![Woekflow image](https://github.com/yashodeepchikte/Multi-Template-Matching/blob/master/main/Assets/images/workflow.JPG)


# Dataset [Link](https://drive.google.com/drive/folders/1-szmxxcJeZ-On1i-kme21qYcNUawJxTY?usp=sharing)
We curated this dataset from another dataset :- <br/>
Cellular detection in fluorescence microscopy acquisition and analysis by <br/>
Waithe D, Brown JM, Reglinski K, Diez-Sevilla I, Roberts D, Eggeling C. 

Subject_01 contains 40 subjects images and 30 templates.
Subject_02 contains 96 subjects images and 28 templates.

The data set consists of various images of medaka and zebrafish embryos. 
Every image consists of a minimum number of organisms mainly four. 
Every subject provided has a different orientation of the microorganism, some of them are overlapping each other. 

The following operation is performed on the dataset:
1.Data images are stored in a folder named subject. <br/>
2.From a given set some templates are manually created using cropping and some enhanced Photoshop technique and are made sure that they are of proper scaling.<br/>
3.These extracted images are further used as input in one of the template generator functions which rotate the template from 0-90 degrees with 10 degrees of each rotation, further, these images are flipped x, flipped y, flipped xy.<br/>
4.All the images obtained above then go through the process of photo enhancement technique which mainly include changes in contrast level, brightness level, color correction, sharpness level, etc.<br/>
5.All the above images are stored in a folder named template. These images are further used for template matching.<br/>

**To use this dataset download the dataset files from this [link](https://drive.google.com/drive/folders/1-szmxxcJeZ-On1i-kme21qYcNUawJxTY?usp=sharing)**  <br/> 
**Extract it and place the subject_01 and subject_02 folders in imputs folder that is in the main folder**<br/> 
**Make sure that in the inputs folder you put the subject_01 and subject_02 folders and not the dataset folder**<br/> 


# Sample images
![Sample Images](https://github.com/yashodeepchikte/Multi-Template-Matching/blob/master/main/Assets/images/sample_images.JPG)


# Results --> 
## Embrio
![Embrio results](https://github.com/yashodeepchikte/Multi-Template-Matching/blob/master/main/Assets/images/embrio_results.JPG)<hr/>
![Embrio analysis](https://github.com/yashodeepchikte/Multi-Template-Matching/blob/master/main/Assets/images/Table.JPG)

# Zebrafish 
![Zebra fish predictions](https://github.com/yashodeepchikte/Multi-Template-Matching/blob/master/main/Assets/images/table2.JPG)
![Zebra-fish results](https://github.com/yashodeepchikte/Multi-Template-Matching/blob/master/main/Assets/images/Zebra_results.JPG)



## Dependencies
This is the list of dependencies for running this application.


 * **Opencv**

 * **Pandas**
 * **Numpy**
 * **Scipy**
 * **Matplotlib**
 
