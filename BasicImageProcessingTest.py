import cv2
import numpy as np

#gives path for image being read
img = cv2.imread('Assets/geforce-rtx-minecraft-disclaimer-og-1200x630.jpg')

#shows image as it
cv2.imshow('ColoredImage', img)

#gives an unlimited time limit where upon pressing any key closes window displaying image
cv2.waitKey(0)
cv2.destroyWindow('ColoredImage')

#0 is the mode for imread function: IMREAD_GRAYSCALE
grayImage = cv2.imread('Assets/geforce-rtx-minecraft-disclaimer-og-1200x630.jpg', 0)
print(grayImage.shape)
cv2.imshow('grayImage', grayImage)

cv2.waitKey(0)
cv2.destroyWindow('grayImage')

grayMatrix = np.asarray(grayImage)
print(grayMatrix)

#set each element of the matrix/array as a value between 1 and 0
# contingent on the values of other elements

normalizedMatrix = grayMatrix / 255
print(normalizedMatrix)
cv2.imshow('normImage', normalizedMatrix)
cv2.waitKey(0)
cv2.destroyWindow('normImage')

transposedImage = cv2.imshow('transposedImage', np.transpose(normalizedMatrix))

cv2.waitKey(0)
cv2.destroyWindow('transposedImage')

mask1 = np.where(normalizedMatrix < 0.3, 1, 0)
mask1 = np.float32(mask1)
#uint8 0-255
#float32 0-1
print(mask1)
cv2.imshow('mask1', mask1)
cv2.waitKey(0)
cv2.destroyWindow('mask1')

mask2 = np.where((normalizedMatrix <= 0.7) & (normalizedMatrix >= 0.3), 1, 0)
mask2 = np.float32(mask2)
cv2.imshow('mask2', mask2)
cv2.waitKey(0)
cv2.destroyWindow('mask2')

mask3 = np.where(normalizedMatrix > 0.7, 1, 0)
mask3 = np.float32(mask3)
cv2.imshow('mask3', mask3)
cv2.waitKey(0)
cv2.destroyWindow('mask3')
