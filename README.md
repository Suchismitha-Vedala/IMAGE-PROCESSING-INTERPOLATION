

1.	Resample

Given an image and the factor by which the image has to be scaled along the x and y directions and the interpolation method
a.	Nearest Neighbor: 
In the nearest neighbor interpolation we first determine the size of the new image which will have the size of the original image scaled by the factor given. We then create an array mage of the new size and fill it with zeros. 
For every pixel of the new image , we assign the pixel value of the old image closest to the current image. This is done by following: we divide every pixel coordinates of the old image with fx and fy along the width and height directions and find the intensity value of the old image with these new coordinates and assign this value to the original pixel coordinates of the new image.
This process is repeated until all pixel values of new image are assigned.


b.	Bilinear
In the Bilinear interpolation we first determine the size of the new image which will have the size of the original image scaled by the factor given. We then create an array mage of the new size and fill it with zeros similarly like in a.
However for bilinear interpolation, the intensity value at a pixel is computed by computing the linear interpolation twice around the surrounding pixels.
For every given pixel coordinate i,j in the new image, we first compute the surrounding coordinates.
We divide each pixel value with fx and fy respectively.
The four points are calculated as follows:
1.	We use floor to calculate lower bound points since floor returns the lower value after division.(x1,y1)
2.	We use ceil to calculate upper bound points since ceil returns the upper bound after division(x2,y2)

Cases to consider:
If (x1==x2)or (y2==y1)
This case gives division by zero, here we make y2=y1+1 or x2=x1+1
If(x2==width of image) or (y2==height of image)
This case gives integer out of bounds. So we make 
X2=w-1
And x1=x2-1
Similarly y2=h-1
Y1=y2-1
We find 4 points(x1,y1),(x2,y1),(x1,y2),(x2,y2)

Then we compute the linear interpolation between (x1,y1),(x2,y1) and (x1,y2),(x2,y2)
Finally we interpolate the intensity value between these two values and assign the value to the pixel coordinates in the new image.
This process is repeated until all pixel values of new image are assigned.


Linear interpolation:

This method is called by the bilinear interpolation. For given (x1,y1),(x2,y1) with intensity I1 and I2, the intensity I at point x,y is given by
I=(((x2-x)/(x2-x1))*I1)+(((x-x1)/ x2-x1))*)*I2)
