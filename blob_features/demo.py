import cv2
import numpy as np
im = cv2.imread('screenshots/blob_shape.jpg',cv2.IMREAD_GRAYSCALE)
# Setup SimpleBlobDetector parameters.
params = cv2.SimpleBlobDetector_Params()

# Filter by Area.
params.filterByArea = True
params.minArea = 100
params.maxArea =100000

# Don't filter by Circularity
params.filterByCircularity = False

# Don't filter by Convexity
params.filterByConvexity = False

# Don't filter by Inertia
params.filterByInertia = False


# Create a detector with the parameters
detector = cv2.SimpleBlobDetector_create(params)

# Detect blobs.
keypoints = detector.detect(im)

# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures
# the size of the circle corresponds to the size of blob
im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

print(im_with_keypoints)

cv2.imshow("Image with center",im_with_keypoints);
cv2.waitKey(0);