import cv2
import numpy as np
from matplotlib import pyplot as plt
np.seterr(divide='ignore', invalid='ignore')
from PIL import Image

class binary_image:

    def compute_histogram(self, image):
        """Computes the histogram of the input image
        takes as input:
        image: a grey scale image
        returns a histogram"""
        img=cv2.imread(image,0)
        w,h=img.shape
        hist = [0]*256
        for i in range(w):
            for j in range(h):
                hist[img[i,j]]=hist[img[i,j]]+1
        


        return hist

    def find_optimal_threshold(self, hist):
        """analyses a histogram it to find the optimal threshold value assuming a bimodal histogram
        takes as input
        hist: a bimodal histogram
        returns: an optimal threshold value"""

        threshold = 0
        l=[]
        t_in=int(255/2)
        l.append(t_in)
        while((len(l) == len(set(l)))==True):
            s=0
            for i in range(t_in):
                s=s+(i*hist[i])
            p=0
            for j in range(t_in):
                p=p+hist[j]
            e1=float(s/p)
            s1=0
            for i in range(t_in,256):
                s1=s1+(i*hist[i])
            p1=0
            for j in range(t_in,256):
                p1=p1+hist[j]
            e2=float(s1/p1)
            e=(e1+e2)/2
            l.append(e)
            t_in=int(e)
        
        optimal=l[len(l)-1]
        
        return optimal

    def binarize(self, image):
        """Comptues the binary image of the the input image based on histogram analysis and thresholding
        take as input
        image: an grey scale image
        returns: a binary image"""
        img=cv2.imread(image,0)
        w,h=img.shape
        new_img=np.zeros((w,h),np.uint8)
        #FIND OPTIMAL THRESHOLD OF IMAGE
        H=self.compute_histogram(image)
        optimal = self.find_optimal_threshold(H)
        for i in range(w):
            for j in range(h):
                if (img[i,j]>=optimal):
                    new_img[i,j]=255
                else:
                    new_img[i,j]=0
        
        
        

        return new_img


