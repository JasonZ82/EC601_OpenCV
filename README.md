# EC601_OpenCV
## Exercise 1
How does a program read the cvMat object, in particular, what is the order of the pixel structure?
cvMat is a matrix structure, It stores pixel values of an image in the matrix. A program read the cvMat object by accessing the particular
pixel point, from entry point(0,0) at the top left of the matrix. Then it will read the type of the data.The order of the pixel structure
should be bit depth, colorspaces, number of different color channels.

## Exercise 2
1. ColorImage.cpp is a program that takes a look at colorspace conversions in OpenCV. Run the code in ColorImage.cpp and comment on the outputs. Implement the same thing in Python and save each image.
In this exercise, I choosed babbon.jpg to implement. After running the code, the image broken into several different colorspaces were shown. We can see 9 different outputs that are red, green, blue, Y, Cr, Cb, Hue, Saturation and value colorspaces.
2. Print out the values of the pixel at (20,25) in the RGB, YCbCr and HSV versions of the image. What are the ranges of pixel values in each channel of each of the above mentioned colorspaces?
RGB value:  [102 165 156]
YCrCb value:  [155 129  98]
hsv value:  [ 34  97 165]

Ranges:All of above are 0-225.

## Excercise 3
1. Look at the code in Noise.cpp and implement the code in Python. Also, print the results for different noise values in the Gaussian case,  mean =0, 5, 10, 20 and sigma = 0, 20, 50, 100 and for the salt-and-pepper case, pa = 0.01, 0.03, 0.05, 0.4 and pb = 0.01, 0.03, 0.05, 0.4.

2. Change the kernel sizes for all the filters with all different values for noises and print the results for 3x3, 5x5 and 7x7 kernels. Comment on the results. Which filter seems to work "better" for images with salt-and-pepper noise and gaussian noise?
For Gaussiannoise images,the Gaussian filter works better.
For Salt-and-pepper images,the Median filter works better.


