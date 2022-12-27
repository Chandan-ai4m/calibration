import cv2
import numpy as np

# Load the image and convert it to grayscale
image = cv2.imread('calibresult16.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Threshold the image to create a binary image with white pixels for the black pixels and black pixels for the rest of the image
ret, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

# Find the contours in the image
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
l=[]
for arr in contours:
    m=np.amax(arr, axis=1)
    l.append(list(m[0]))
print(l)
l1=[i[1] for i in l]
print(l1)
maxima = []
for i in range(1, len(l1) - 1):
    if l1[i] > l1[i-1] and l1[i] > l1[i+1]:
        maxima.append(l1[i])
if max(l1) not in maxima:
    maxima.append(max(l1))
print(maxima)
#     maxh=max(np.amax(arr, axis=0),maxh) 
cv2.drawContours(image, contours, -1, (0, 255, 0), 2)

# show the image
imj =  cv2.resize(image, (500, 500), interpolation=cv2.INTER_LINEAR)
cv2.imshow('image',imj )
cv2.waitKey(0)
cv2.destroyAllWindows()
# print(maxh)
# Iterate through the contours and filter out the ones that are not likely to be the rounded rectangular shape
for c in contours:
    # Calculate the area of the contour
    area = cv2.contourArea(c)

    # Calculate the aspect ratio of the bounding rectangle of the contour
    x, y, w, h = cv2.boundingRect(c)
    aspect_ratio = w / h

