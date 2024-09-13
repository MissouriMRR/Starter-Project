#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This is one of the Intro Projects for the Missouri S&T Multirotor Design Team.
The link to the project can be found here:
https://missourimrr.github.io/docs/vision/opencv/blue_tomatoes/

This is my implementation of the project. The goal is to turn the tomatoes in
this image blue. The requirements are below.
"""

##############################################################################
#                               Requirements                                 #
##############################################################################
# Read the image into a numpy array using cv2, setting up cv2 for clustering #
# and masking the photo use cv2 to mask all the reds in the tomato and turn  #
# those tomatoes blue output the image and save it                           #
##############################################################################

## Imports
# Built-in
import os
import logging
# External
import cv2 # OpenCV
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Set up logging
logging.basicConfig(level=logging.INFO)

# This is all done in one function but it could be broken up into multiple
# and/or classes, which helps with readability and maintainability.
# I am just doing this for simplicity
def main() -> None:

    ## Read the image into a numpy array
    # - os.path.join() creates a file path that is compatible with the OS using
    # strings passed in as arguments
    # - os.getcwd() gets the current working directory
    # These are used to get a path to the image file from the working directory
    # which I have set as the root of this git repository
    img = mpimg.imread(os.path.join(os.getcwd(), "Vision", "Project1", "salad.jpg"))

    ## Set up clustering on the image
    # Vectorize the image data
    logging.info("Vectorizing the image data...")
    vectorized = img.reshape((-1, 3))
    vectorized = np.float32(vectorized)

    # Set up termination criteria for cv2.kmeans
    termination_criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    K = 9
    _, label, center = cv2.kmeans(vectorized, K, bestLabels=None, criteria=termination_criteria, attempts=10, flags=0)

    k_image = np.uint8(center)[label.flatten()]
    k_image = k_image.reshape((img.shape))

    ## Set up a mask for the reds
    # Convert the image to HSV
    logging.info("Converting the image to HSV...")
    img_hsv = cv2.cvtColor(k_image, cv2.COLOR_RGB2HSV)

    # Set up the lower and upper bounds for the reds
    lower_red = np.array([0, 50, 100])
    upper_red = np.array([10, 255, 255])

    # Create the mask
    logging.info("Creating a mask for reds...")
    mask = cv2.inRange(img_hsv, lower_red, upper_red)
    mask = np.dstack((mask, mask, mask))

    # Apply the mask
    logging.info("Applying the mask...")
    img_array = np.copy(img)
    img_array = np.where(mask==(0, 0, 0), img_array, 255 - img_array)

    # Ask the user if they want to save the image or just display it
    logging.info("Image processing complete.")
    save = input("Do you want to save the image? [Y/n]:\n->: ")
    if save.lower() == "y" or save == "":
        # Save the image
        mpimg.imsave(os.path.join(os.getcwd(), "Vision", "Project1", "blue_tomatoes.jpg"), img_array)
    else:
        # Display the image
        plt.imshow(img_array)
        plt.show()

if __name__ == "__main__":
    main()
