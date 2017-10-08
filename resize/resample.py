import cv2
import sys
import numpy as np
from matplotlib import pyplot as plt
np.seterr(divide='ignore', invalid='ignore')
from PIL import Image
sys.path.insert(0,'/Users/suchi/Desktop/Fall 2017/DIP/GIt/resize')
from interpolation import interpolation 
class resample:

    def resize(self, image, fx = None, fy = None, interpolation = None):
        """calls the appropriate funciton to resample an image based on the interpolation method
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        interpolation: method used for interpolation ('either bilinear or nearest_neighbor)
        returns a resized image based on the interpolation method
        """

        if interpolation == 'bilinear':
            return self.bilinear_interpolation(image, fx, fy)

        elif interpolation == 'nearest_neighbor':
            return self.nearest_neighbor(image, fx, fy)

    def nearest_neighbor(self, image, fx, fy):
        """resizes an image using bilinear interpolation approximation for resampling
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        returns a resized image based on the nearest neighbor interpolation method
        """
        #print image.shape
        img = cv2.imread(image)
        #plt.imshow(img)
        #plt.show()
        w,h,c = img.shape

        #print w, h
        #print type(fx),type(fy)
        l=float(fx)
        m=float(fy)
        new_w=int(l*w)
        new_h=int(m*h)
        print 'width','height', w,h,c,new_w,new_h
        b=np.zeros((new_h,new_w,c),np.uint8)
        for i in range(new_w):
            for j in range(new_h):
                b[j,i,:]=img[int(i/l),int(j/m),:]

        #Write your code for nearest neighbor interpolation here

        return b


    def bilinear_interpolation(self, image, fx, fy):
        """resizes an image using bilinear interpolation approximation for resampling
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        returns a resized image based on the bilinear interpolation method
        """

        # Write your code for bilinear interpolation here
        img = cv2.imread(image,1)
        w,h,c = img.shape
        w1=w
        h1=h
        l=float(fx)
        m=float(fy)
        new_w=int(l*w)
        new_h=int(m*h)
        print w,h,new_w,new_h
        b=np.zeros((new_h,new_w,c),np.uint8)
        i=0
        j=0
        for i in range(new_w):
            for j in range(new_h):
                x1=int((np.floor(i/l)))
                x2=int((np.ceil(i/l)))
                if(x1 == x2):
                    x1=x2-1
                y1=int((np.floor(j/m)))
                y2=int((np.ceil(j/m)))
                if(y1 == y2):
                    y1=y2-1
                if(y2==h):
                    y2=h-1
                    y1=h-2
                if(x2==w):
                    x2=w-1
                    x1=w-2
                x=int(i/l)
                y=int(j/m)
                xi=x
                yi=y
                I1=img[x1][y1][:]
                I2=img[x2][y1][:]
                I3=img[x1][y2][:]
                I4=img[x2][y2][:]
                pt1=(x1,y1,I1)
                #print pt1[0], pt1[1],pt1[2]
                #print pt2[0]-pt1[0], pt3[1]-pt2[1],pt2[2]
                pt2=(x2,y1,I2)
                pt3=(x1,y2,I3)
                pt4=(x2,y2,I4)
                unknown=(xi,yi)
     
          
                bb_obj=interpolation()
                print 'calling bilinear'
                value=bb_obj.bilinear_interpolation(pt1,pt2,pt3,pt4,unknown)
                print value
                b[j,i,:]=value
  
                     
                
      
        return b

