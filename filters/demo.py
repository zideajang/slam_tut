import cv2
import numpy as np
from matplotlib import pyplot as plt

# print(cv2.__version__)

def demo_one():
    img = cv2.imread('screenshots/opencv-logo.png')
    # print(img)
    kernel = np.ones((5,5),np.float32)/25
    dst = cv2.filter2D(img,-1,kernel)

    plt.subplot(121),plt.imshow(img),plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
    plt.xticks([]), plt.yticks([])
    plt.show()

def main():
    pass

if __name__ == '__main__':
    main()