import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

img = mpimg.imread('/home/.ssh/Starter-Project/Vision/Project1/salad.jpg')
salad = np.copy(img) # 190, 155, 140 -- 75, 70, 70
reds = ((salad[:, :, 0] >= 190) & (salad[:, :, 1] <= 150) & (salad[:, :, 2] <= 140) | ((salad[:, :, 0] >= 75) & (salad[:, :, 1] <= 70) & (salad[:, :, 2] <= 70)))
salad[reds, 2] = salad[reds, 0]
salad[reds, 0] = 0

# get rid of most of the stray blue pixels
edge = img.shape[1] // 4
salad[:, :edge] = img[:, :edge]

plt.imshow(salad)
plt.show()
