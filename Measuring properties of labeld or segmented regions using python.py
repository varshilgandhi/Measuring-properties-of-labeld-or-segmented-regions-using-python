# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 11:35:48 2021

@author: abc
"""

"""

RegionProps


"""
from skimage import measure, io, img_as_ubyte
import matplotlib.pyplot as plt
from skimage.color import label2rgb , rgb2grey
import numpy as np

#Read our image and convert it into rgb2gray
image = img_as_ubyte(rgb2grey(io.imread("cast_iron.jpg")))

#Let's THRESHOLD THIS image 
from skimage.filters import threshold_otsu
threshold = threshold_otsu(image)

#Let's label this image
label_image = measure.label(image < threshold, connectivity=image.ndim)

#Let's see labeled image
plt.imshow(label_image)

#Let's convert label2rgb for better ploting and understanding
image_label_overlay = label2rgb(label_image, image=image)
plt.imshow(image_label_overlay)

#Apply RegionProps
props = measure.regionprops_table(label_image, image, 
                                  properties=['label', 
                                              'area', 'equivalent_diameter',
                                              'mean_intensity', 'solidity'])

#Let's see props dataframe
import pandas as pd
df = pd.DataFrame(props)
print(df.head())













