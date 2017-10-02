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
        img = cv2.imread(image,0)
        #plt.imshow(img)
        #plt.show()
        w,h,c = a.shape
        new_w=int(w*fx)
        new_h=int(h*fy)
        b=np.zeros((new_h,new_w,c),np.uint8)
        for i in range(new_w):
            for j in range(new_h):
                b[j,i,:]=img[int(i/fx)][int(j/fy)][:]

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
        new_w=int(w*fx)
        new_h=int(h*fy)
        b=np.zeros((new_h,new_w,c),np.uint8)
        for i in range(new_w):
            for j in range(new_h):
                x1=int((np.floor(i/fx)))
                x2=int((np.ceil(i/fx)))
                if (x1 == 0):
                    x1=1
                x= 0
                y1=int(np.floor(j/fy))
                y2=int(np.ceil(j/fy))
                if (y1 == 0):
                    y1=1
                y= 0
                I1 = img[x1,y1,:]
                I2 = img[x2,y1,:]       
                I3 = img[x1,y2,:]
                I4 = img[x2,y2,:]  
                y = int((j/fx))
                I5 = ((I3*y)+(I1*(1-y)))
                I6 = ((I4*y)+(I2*(1-y))) 
                b[j,i,:] = ((I6*x)+(I5*(1-x)))
    

        return B

