import cv2
import numpy as np

print('packadge imported')

"""" here i am demonstrating how to resize an image """


img = cv2.imread('resources/images/view1.jpeg')

imageResize = cv2.resize(img, (100, 200))

cv2.imshow("output", imageResize)
cv2.waitKey(0)
print(imageResize.shape)


"""" here i am converting image2 to a grey color"""

img2 = cv2.imread('resources/images/view2.jpeg')
grey = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
resized = cv2.resize(img2, (200, 200))
cv2.imshow("greycolor", resized)
cv2.waitKey(0)


"""" here i am converting image3 to blur """

img3 = cv2.imread('resources/images/view3.jpeg')
bluring = cv2.GaussianBlur(img3, (7, 7), 0)
cunny = cv2.Canny(img3, 100, 100)
resized = cv2.resize(bluring, (150, 200))

cv2.imshow("blur", img3)
cv2.imshow("blur", bluring)
cv2.imshow("canny", cunny)
cv2.imshow("window", resized)

cv2.waitKey(0)

"""" here i am converting image4 to only edges """

img4 = cv2.imread('resources/images/view3.jpeg')
bluring = cv2.GaussianBlur(img4, (7, 7), 0)
cunny = cv2.Canny(img4, 100, 100)

cv2.imshow("blur", img4)
cv2.imshow("blur", bluring)
cv2.imshow("cunny", cunny)
cv2.waitKey(0)

"""" here i am converting image5 reducing  edges to low pixels """

img4 = cv2.imread('resources/images/view3.jpeg')
bluring = cv2.GaussianBlur(img4, (7, 7), 0)
cunny = cv2.Canny(img4, 150, 90)
resized = cv2.resize(cunny, (200, 200))

cv2.imshow("blur", img4)
cv2.imshow("blur", bluring)
cv2.imshow("cunny", cunny)
cv2.imshow('window', resized)
cv2.waitKey(0)


"""" here i am converting image6 to image dialation"""

kernel = np.ones((5, 5), np.uint8)

img6 = cv2.imread('resources/images/view6.jpeg')
bluring = cv2.GaussianBlur(img6, (7, 7), 0)
cunny = cv2.Canny(img6, 150, 90)
dilating = cv2.dilate(cunny, kernel, iterations=1)
resized = cv2.resize(dilating, (150, 100))
print(resized.shape)

cv2.imshow("blur", img4)
cv2.imshow("blur", bluring)
cv2.imshow("cunny", cunny)
cv2.imshow('dilate', dilating)
cv2.imshow('window', resized)
cv2.waitKey(0)


"""" here i am demonstrating how to crop an image by croping image7"""

img7 = cv2.imread('resources/images/view7.jpeg')
crop = img7[0:50, 50:50]

cv2.imshow('img7cropped', img7)
cv2.waitKey(0)


"""" here i am demonstrating how to change background image of image8"""

img8 = cv2.imread('resources/images/view8.jpeg')
hsv = cv2.cvtColor(img8, cv2.COLOR_BGR2HSV)
resized = cv2.resize(hsv, (150, 100))


cv2.imshow('background', resized)
cv2.imshow("hsv", hsv)
cv2.waitKey(0)
