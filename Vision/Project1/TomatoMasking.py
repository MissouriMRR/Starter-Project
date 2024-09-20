import cv2
import numpy as np

# read the image into a numpy array using cv2
original = cv2.imread("salad.jpg")

# Setting up cv2 for clustering and masking the photo
hsv = cv2.cvtColor(original, cv2.COLOR_BGR2HSV)
lower_red = np.array([-20, 140, 60])
upper_red = np.array([20, 255, 255])

# use cv2 to mask all the reds in the tomato
mask = cv2.inRange(hsv, lower_red, upper_red)

# turn tomatoes blue
bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
for row in range(len(original)):
    for px in range(len(original[0])):
        if (mask[row][px] == 255):
            bgr[row][px] = 255 - bgr[row][px]

# output the image and save it
cv2.imwrite("blue_tomato.jpg", bgr)
cv2.imshow("result", bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()