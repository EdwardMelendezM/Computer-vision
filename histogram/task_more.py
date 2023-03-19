import cv2
import numpy as np
import matplotlib.pyplot as plt
image = cv2.imread("src/saitama.jpg")

# convert image from RGB to HSV
img_hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)

# Histogram equalisation on the V-channel
img_hsv[:, :, 2] = cv2.equalizeHist(img_hsv[:, :, 2])

# convert image back from HSV to RGB
image = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2RGB)
cv2.imshow('Comparison', image)
cv2.waitKey(0)
