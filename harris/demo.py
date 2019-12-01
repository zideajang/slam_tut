import cv2
import numpy as np

img = cv2.imread('img/jay.png')

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)

dst = cv2.cornerHarris(gray,3,3,0.04)

print(dst.shape)

img[dst > 0.01 * dst.max()] = [0,0,255]

cv2.imshow('dst',img)
if cv2.waitKey(0) & 0xff == ord('q'):
    cv2.destroyAllWindows()