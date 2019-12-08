# coding=utf-8
import cv2
import numpy as np
import matplotlib.pyplot as plt

def main():
    path = "img/lena.png"
    img = cv2.imread(path,1)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

    # k = np.array(([0,0,0],[0,1,0],[0,0,0]),np.float32)
    # edge detection
    # 边缘检测
    # k = np.array(([1,0,-1],
    #             [0,0,0],
    #             [-1,0,1]),np.float32)
    # 图片锐化
    # k = np.array(([0,-1,0],
    #             [-1,5,-1],
    #             [0,-1,0]),np.float32)
    k = np.array(([1,2,1],
                [2,4,2],
                [1,2,1]),np.float32) / 16.0
    # k = np.array(np.ones((3,3),np.float32))
    # print(k)
    '''
    [[0. 0. 0.]
    [0. 1. 0.]
    [0. 0. 0.]]
    '''

    output = cv2.filter2D(img,-1,k)
    
    # -1 表示输出图片大小和输入图片大小一致

    plt.subplot(1,2,1)
    plt.imshow(img)
    plt.title("Original Image")

    plt.subplot(1,2,2)
    plt.imshow(output)
    plt.title("Filtered Image")

    plt.show()

if __name__ == '__main__':
    main()
    