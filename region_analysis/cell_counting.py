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
        new_img = cv2.imread(image,0)
        w,h=new_img.shape
        img=np.zeros((w,h),np.uint8)
        H=binary_image().compute_histogram(image)
        optimal=binary_image().find_optimal_threshold(H)
        for i in range(w):
            for j in range(h):
                if (new_img[i,j]>=optimal):
                    img[i,j]=0
                else:
                    img[i,j]=255
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

    def compute_statistics(self, region):
        """Compute cell statistics area and location
        takes as input
        region: a list of pixels in a region
        returns: area"""
        regions=blob_coloring(image)
        region_statistics=dict()
        stats=[]
        centroid=[]
        for k,v in regions.iteritems():
            l=len(v)
            area=l
            x_cord=[v[i][0] for i in range(len(v))]
            y_cord =[v[i][1] for i in range(len(v))]
            xc=(sum(x_cord))/l
            yc=(sum(y_cord))/l
            cent=[xc,yc]
            centroid.append(cent)
            area=l
            stats.append([area,cent])
            region_statistics[k]=[area,cent]
            print "Region:",k,"  Area:",len(v),"  Centroid:",[xc,yc]
            
            



        # Please print your region statistics to stdout
        # <region number>: <location or center>, <area>
        # print(stats)

        return region_statistics

    def mark_regions_image(self, image, stats):
        """Creates a new image with computed stats
        takes as input
        image: a list of pixels in a region
        stats: stats regarding location and area
        returns: image marked with center and area"""
        for a in stats.keys():
        cv2.putText(image, '*' + repr(a) + ',' + repr(stats[a][0]), (int(stats[a][1][1]), int(stats[a][1][0])), cv2.FONT_HERSHEY_SIMPLEX, 0.25, 100)



        return image

