import numpy as np

class binary_image:

    def compute_histogram(self, image):
        """Computes the histogram of the input image
        takes as input:
        image: a grey scale image
        returns a histogram"""

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
        t_in=int(255/2)
        s=0
        for i in range(t_in):
            s=s+(i*hist[i])
        p=0
        for j in range(t_in):
            p=p+hist[t_in]
        e1=s/p
        s1=0
        for i in range(t_in,256):
            s1=s1+(i*hist[i])
        p1=0
        for j in range(t_in,256):
            p1=p1+hist[t_in]
        e2=s1/p1
        E1=[]
        for i in range(t_in):
            E1.append((i*hist[i])/e1)
        E2=[]
        for i in range(t_in,256):
            E2.append((i*hist[i])/e2)
        optimal=(np.float(sum(E1)) / max(len(E1), 1)  + np.float(sum(E2)) / max(len(E2), 1))/2


        return optimal

    def binarize(self, image):
        """Comptues the binary image of the the input image based on histogram analysis and thresholding
        take as input
        image: an grey scale image
        returns: a binary image"""

        bin_img = image.copy()

        return bin_img


