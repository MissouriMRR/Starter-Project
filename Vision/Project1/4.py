import numpy as np

## pip install matplotlib
import matplotlib.image as mpimg  # mpimg.imread(path) to read in an image
import matplotlib.pyplot as plt  # plt.imshow(np.array) to show an image

# read in image
img = mpimg.imread("salad.jpg")

# Convert BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_RGB2HSV)

# define range of blue color in HSV
lower_blue = np.array([11,91,53])
upper_blue = np.array([0,50,84])

# Threshold the HSV image to get only blue colors
mask = cv.inRange(hsv, lower_blue, upper_blue)

# Bitwise-AND mask and original image
res = cv.bitwise_and(img,img, mask= mask)
res = cv.cvtColor(img, cv.COLOR_HSV2RGB)
# show image
plt.imshow(mask, cmap="gray")
plt.show()