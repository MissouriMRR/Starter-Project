# read the image into a numpy array using cv2

# Setting up cv2 for clustering and masking the photo

# use cv2 to mask all the reds in the tomato and turn those tomatoes blue

# output the image and save it

import numpy as np

import cv2
import matplotlib.pyplot as plt

# Load image
salad = cv2.imread('salad.jpg')

# Convert the image from BGR to HSV color space
hsv_salad = cv2.cvtColor(salad, cv2.COLOR_BGR2HSV)

# Define range for finding red 
lower_red1 = np.array([
upper_red2 = np.array([180, 255, 255])

# Create image masks to detect red
mask1 = cv2.inRange(hsv_salad, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv_salad, lower_red2, upper_red2)

# Combine the masks
red_mask = cv2.bitwise_or(mask1, mask2)

# Remove noise with morphological trans
kernel = np.ones((5, 5), np.uint8)
red_mask = cv2.morphologyEx(red_mask, cv2.MORPH_OPEN, kernel)

# Change red to blue
salad[red_mask > 0] = [255, 0, 0,] #BGR [255 0 0] -> blue

# Display the image
cv2.imshow('Blue Tomatoes', salad)
cv2.waitKey(0)
cv2.destroyAllLWindows()0, 80, 50])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([150, 80, 50])

