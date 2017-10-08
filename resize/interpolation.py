import cv2
import numpy as np
from matplotlib import pyplot as plt
np.seterr(divide='ignore', invalid='ignore')
from PIL import Image

class interpolation:

    def linear_interpolation(self, pt1, pt2, unknown):
        """Computes the linear interpolation for the unknown values using pt1 and pt2
        take as input
        pt1: known point pt1 and f(pt1) or intensity value
        pt2: known point pt2 and f(pt2) or intensity value
        unknown: take and unknown location
        return the f(unknown) or intentity at unknown"""
        I1=pt1[2]
        I2=pt2[2]
        x=unknown[0]
        y=unknown[1]
        x1=pt1[0]
        x2=pt2[0]
        denom=x2-x1
        I=(((x2-x)/denom)*I1)+(((x-x1)/denom)*I2)
        return I

        #Write your code for linear interpolation here

    def bilinear_interpolation(self, pt1, pt2, pt3, pt4, unknown):
        """Computes the linear interpolation for the unknown values using pt1 and pt2
        take as input
        pt1: known point pt1 and f(pt1) or intensity value
        pt2: known point pt2 and f(pt2) or intensity value
        pt1: known point pt3 and f(pt3) or intensity value
        pt2: known point pt4 and f(pt4) or intensity value
        unknown: take and unknown location
        return the f(unknown) or intentity at unknown"""
        I11=self.linear_interpolation(pt1,pt2,unknown)
        I12=self.linear_interpolation(pt3,pt4,unknown)
        y1=pt1[1]
        y2=pt3[1]
        y=unknown[1]
        denom=y2-y1
        
        
        I33=(((y2-y)/denom)*I11)+(((y-y1)/denom)*I12)
        

        # Write your code for bilinear interpolation here
        # May be you can reuse or call linear interpolatio method to compute this task

        return I33
