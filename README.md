# EC601_OpenCV
## Exercise 1
How does a program read the cvMat object, in particular, what is the order of the pixel structure?
cvMat is a matrix structure, It stores pixel values of an image in the matrix. A program read the cvMat object by accessing the particular
pixel point, from entry point(0,0) at the top left of the matrix. Then it will read the type of the data.The order of the pixel structure
should be bit depth, colorspaces, number of different color channels.
