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


def create_kernel():
    arr = np.array([0,0,0,0,0,1,0,0,0])
    return arr.reshape(3,3) 

def convs(img,kernel):
    h = img.shape[0]
    w = img.shape[1]
    print(w,h)

def denoise():
    image = cv2.imread("img/cameramannoise.jpg")
    # apply the 3x3 mean filter on the image
    kernel = np.ones((3,3),np.float32)/9
    processed_image = cv2.filter2D(image,-1,kernel)
    # display image
    cv2.imshow('Mean Filter Processing', processed_image)
    # save image to disk
    # cv2.imwrite('processed_image.png', processed_image)
    # pause the execution of the script until a key on the keyboard is pressed
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def move_img_by_filter(img):
    conv = cnp.array([0,0,0,0,0,1,0,0,0]).reshape(3,3)
    h = img.shape[0]
    w = img.shape[1]
    for i in range(1,h-1):
        for j in range(1,w-1):
            print(img[i,j])
            img[i,j] = (img[i-1,j-1] * conv[0,0] + img[i-1,j]*conv[0,1] + img[i-1,j+1]*conv[0,2] +
                img[i,j-1] * conv[1,0] + img[i,j]*conv[1,1] + img[i,j+1]*conv[1,2] +
                img[i+1,j-1] * conv[2,0] + img[i+1,j]*conv[2,1] + img[i+1,j+1]*conv[2,2])
            # print(img[i,j])
    return img


def sobel_demo():
    img = cv2.imread('img/dave.jpg',0)

    laplacian = cv2.Laplacian(img,cv2.CV_64F)
    sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
    sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)

    plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
    plt.title('Original'), plt.xticks([]), plt.yticks([])
    plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')
    plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
    plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
    plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
    plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
    plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
    plt.show()

def main():
    # sobel_demo()
    # denoise()
    # print(create_kernel())
    # kernel = create_kernel()
    # print(kernel[1,1])
    img = cv2.imread("img/bird.jpg")
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    print(gray)
    # gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # gray_1 = move_img_by_filter(gray)
    # gray_2 = move_img_by_filter(gray_1)
    # gray_3 = move_img_by_filter(gray_2)
    # gray_4 = move_img_by_filter(gray_3)
    # dst = move_img_by_filter(gray_4)
    # cv2.imshow("bird",img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    # print(kernel.shape)
    # convs(img,1)
    # fiture, axarr = plt.subplots(2,2)
    # axarr[0,0].imshow(gray)
    # axarr[0,1].imshow(dst)
    # plt.show()
if __name__ == '__main__':
    main()