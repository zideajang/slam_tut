# coding=utf-8
import numpy as np
import cv2 
from matplotlib import pyplot as plt

# img = np.zeros((200,200),np.uint8)
# cv2.rectangle(img,(0,100),(200,200),(255),-1)
# cv2.rectangle(img,(0,50),(100,100),(127),-1)
# cv2.imshow("img",img)

# plt.hist(img.ravel(),256,[0,256])
# plt.show()

# cv2.waitKey(0)
# cv2.destroyAllWindows()

def split_into_rgb_channels(img):
    red = img[:,:,2] = 0
    green = img[:,:,1] = 0
    blue = img[:,:,0]
    
    cv2.imshow("red",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



def main():
    img = cv2.imread("img/lena.png")
    split_into_rgb_channels(img)

if __name__ == '__main__':
    main()