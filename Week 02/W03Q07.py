#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Week 2 from "Fundamentals of Digital Image and Video Processing"
#
# Question 7
#
# In this problem you will implement spatial-domain low-pass filtering
# using MATLAB, and evaluate the difference between the filtered image
# and the original image using two quantitative metrics called
# Mean Squared Error (MSE) and Peak Signal-to-Noise Ratio (PSNR).
#
#
# Given two N1×N2 images x(n1,n2) and y(n1,n2), the MSE is computed as
# MSE=1N1N2∑N1n1=1∑N2n2=1[x(n1,n2)−y(n1,n2)]2. The PSNR is defined as
# PSNR=10log10(MAX2IMSE), where MAXI is the maximum possible pixel value
# of the images. For the 8-bit gray-scale images considered in this
# problem, MAXI=255. Follow the instructions below to finish this
# problem.
#
# (1) Download the original image from here. The original image is
#     a 256×256 8-bit gray-scale image.
# (2) Convert the original image from type 'uint8' (8-bit integer) to
#     'double' (real number).
# (3) Create a 3×3 low-pass filter with all coefficients equal to 1/9,
#     i.e., create a 3×3 MATLAB array with all elements equal to 1/9.
# (4) Low-pass filter the original image (converted to type 'double')
#     with
#     the filter created in step (3). This can be done using the
#     built-in MATLAB function "imfilter". The function "imfilter" takes
#     three arguments and returns one output. The first argument is the
#     original image (converted to type 'double'); the second argument
#     is the low-pass filter created in step (3); and the third argument
#     is a string specifying the boundary filtering option. For this
#     problem, use 'replicate' (including the single quotes) for the
#     third argument. The output of the function "imfilter" is the
#     filtered image.
# (5) Compute and record the PSNR value between the original image
#     (converted to type 'double') and the filtered image by using the
#     formulae given above.
# (6) Repeat steps (3) through (5) using a 5×5 low-pass filter with all
#     coefficients equal to 1/25. Enter the PSNR values you have
#     obtained from your experiments (The PSNR corresponding to 3×3
#     filter first, followed by the PSNR corresponding to 5×5 filter).
#     Make sure you order the answers correctly and separate them by a
#     space. Enter the numbers to 2 decimal points.
#
# Note: Answers are 29.2951 for 3x3 matrix and 25.7335 for 5x5 matrix

import matplotlib.pyplot as plt
import numpy as np
import scipy.ndimage as ndimage
import Image

def plot(data, title):
    plot.i += 1
    plt.subplot(2,2,plot.i)
    plt.imshow(data)
    plt.gray()
    plt.title(title)

# Usig the original to get the same results
im = Image.open('lena.gif')

# image converted to double with max value of 1
data = np.array(im)/255.0
plot.i = 0
plot(data, 'Original')

# Create the filters
k3 = np.ones((3,3))/9.0
k5 = np.ones((5,5))/25.0

# Now the convolution
lp3 = ndimage.convolve(data, k3, mode='nearest')
lp5 = ndimage.convolve(data, k5, mode='nearest')

mse3 = np.sum(np.power(lp3-data,2))/np.size(data)
mse5 = np.sum(np.power(lp5-data,2))/np.size(data)

#~ PSNR = 10*np.log10(np.power(MAXi,2)/MSE);
psnr3 = 10*np.log10(np.power(1.0,2)/mse3);
psnr5 = 10*np.log10(np.power(1.0,2)/mse5);

print psnr3, psnr5

plot(lp3, '3x3 low-pass')
plot(lp5, '5x5 low-pass')
plt.show()

# other posible modes for borders:
# reflect:  29.2951 25.7315
# constant: 28.3131 24.9244 with cval=0
# nearest:  29.2951 25.7335
# mirror:   29.2872 25.7261
# wrap:     28.8001 25.3345
#
# Answer from matlab:  29.2951 25.7335
# *nearest* is the exact replacement and *reflect* is very close
