# coding=utf-8
import cv2
import numpy as np

# Difference between correlation and convolution
def conv_transform(image):
    image_copy = image.copy()

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            image_copy[i][j] = image[image.shape[0]-i-1][image[1]-j-1]
    return image_copy


def conv(image,kernel):
    # The image will be grayscale otherwise there will be confusion with 3 channel
    kernel = conv_transform(kernel) # to differ it from corelation
    image_h = image.shape[0] #7 row
    image_w = image.shape[1] #7 colum

    kernel_h = kernel.shape[0] #3 row
    kernel_w = kernel.shape[1] #3 colum

    h = kernel_h//2 #integer value
    w = kernel_w //2 #integer value

    image_conv = np.zeros(image.shape)

    for i in range(h, image_h-h):
        for j in range(w,image_w-w):
            sum = 0
            for m in range(kernel_h):
                for n in range(kernel_w):
                    sum = sum + kernel[m][n] * image[i-h+m][j-w+n]
            image_conv[i][j] = sum
    cv2.imshow('convolved_image',image_conv)
    # return image_conv
    cv2.waitKey(0)
    cv2.destroyAllWindows()
img = cv2.imread('img/lena.png',0)

# cv2.imshow('img',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
conv(img,[[-4,0,0][0,0,0][0,0,-4]])
