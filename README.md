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
