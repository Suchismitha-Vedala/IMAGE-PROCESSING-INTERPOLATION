import cv2
import numpy as np
from matplotlib import pyplot as plt
np.seterr(divide='ignore', invalid='ignore')
from PIL import Image
class cell_counting:

    def blob_coloring(self, image):
        
        """Uses the blob coloring algorithm based on 8 pixel window assign region names
        takes a input:
        image: binary image
        return: a list of regions"""
        regions = dict()
        
        w,h=image.shape
        img=np.zeros((w,h),np.uint8)
        
        for i in range(w):
            for j in range(h):
                if (image[i,j]==0):
                    img[i,j]=255
                elif(image[i,j]==255):
                    img[i,j]=0
        k=1
        R=np.zeros((w,h),np.uint32)
        for j in range(h):
            for i in range(w):
                if (img[i,j]!=0):
                    if (i==0 and j>0) :
                        if (R[i, j-1]==0) :
                            R[i, j] = k
                            k = k + 1
                        if (R[i, j - 1] > 0):
                            R[i, j] = R[i, j-1]
                        
                        
                    if (j==0 and i>0) :
                        if (R[i-1,j]>0):
                            R[i,j]=R[i-1,j]
                        if (R[i-1,j]==0):
                            R[i, j] = k
                            k = k + 1
                        
                    if(i-1>=0 and j-1>=0):
                        if( R[i][j-1]>0 and R[i-1][j]==0):
                            R[i,j]=R[i,j-1]
                        if( R[i][j-1]==0 and R[i-1][j]>0):
                            R[i,j]=R[i-1,j]
                        if( R[i][j-1]==0 and R[i-1][j]==0):
                            R[i,j]=k
                            k=k+1
                        if( R[i][j-1]>0 and R[i-1][j]>0):
                            R[i,j]=R[i,j-1]
                            R[i-1,j]=R[i,j-1]
                            p=2
                            q=0
                            while(q==0):
                                if (R[i-p,j]!=0):
                                        R[i-p,j]=R[i-p+1,j]
                                        p=p+1
                                
                                else :
                                        q=1
                       
    
        regions = dict()
   
        for i in range(w):
            for j in range(h):
                if (R[i,j]!=0):
                    if  R[i,j] in regions:
                        regions[R[i,j]].append([i,j])
                    else:
                        regions[R[i,j]]=[[i,j]]

        return regions

    def compute_statistics(self, regions):
        """Compute cell statistics area and location
        takes as input
        region: a list of pixels in a region
        returns: area"""

        centroid=[]
        stats=[]
        region_statistics=dict()
        for k,v in regions.iteritems():
            cent=[]
            xc=yc=0
            x_cord=[]
            y_cord=[]
            l=len(v)
            x_cord=[v[i][0] for i in range(l)]
            y_cord =[v[j][1] for j in range(l)]
            xc=int((sum(x_cord))/l)
            yc=int((sum(y_cord))/l)
            cent=[xc,yc]
            centroid.append(cent)
            area=l
            stats.append([area,cent])
            region_statistics[k]=[area,cent]
            
        statistic_area=dict()
        i=0
        for k,v in region_statistics.iteritems():
            if(v[0]>15):
                statistic_area[k]=v
                print 'Region', k, 'Area', v[0], 'Centroid', v[1]
    



        # Please print your region statistics to stdout
        # <region number>: <location or center>, <area>
        # print(stats)

        return region_statistics,statistic_area

    def mark_regions_image(self, image, stats):
        """Creates a new image with computed stats
        takes as input
        image: a list of pixels in a region
        stats: stats regarding location and area
        returns: image marked with center and area"""
        w,h=image.shape
        img=np.zeros((w,h),np.uint8)
        
        for i in range(w):
            for j in range(h):
                if (image[i,j]==0):
                    img[i,j]=255
                elif(image[i,j]==255):
                    img[i,j]=0
        x_cord=[]
        y_cord=[]
        ar=[]
        for k,v in stats.iteritems():
            
            x_cord.append(v[1][0])
            y_cord.append(v[1][1])
            ar.append(v[0])
     
        for q in range(len(ar)):
                      line='*'+str(ar[q])+","+str(q)
                      cv2.putText(img, line , ((y_cord[q]), (x_cord[q])), cv2.FONT_HERSHEY_SIMPLEX, 0.25, 60)


        return img

