# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

# %% parameters ---------------------------------------------------------------

# original image
file = 'rapperswil.jpg'

# filters
T_gray = np.full((3, 3), 1/3)
T_sepia = np.array([[0.393, 0.769, 0.189],
                    [0.349, 0.686, 0.168],
                    [0.272, 0.534, 0.131]])


# %% read the original image --------------------------------------------------
img_original = plt.imread(file)/255
img_aspectratio = img_original.shape[1]/img_original.shape[0]


# %% apply the filters --------------------------------------------------------
# use @ or np.dot()
img_gray = (img_original @ T_gray.T).clip(0, 1)
img_sepia = np.dot(img_original, T_sepia.T).clip(0, 1)

# %% visualize the images -----------------------------------------------------
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(12, 12/3/img_aspectratio))

for ax, image, title in [(ax1, img_original, 'original'),
                         (ax2, img_gray, 'grayscale'),
                         (ax3, img_sepia, 'sepia')]:
    # plot the image
    ax.imshow(image)
    # remove the axes
    ax.axis('off')
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    # write the title in the upper right corner of the image
    ax.text(1, 1, title, va='top', ha='right', transform=ax.transAxes)

# remove any padding in the figure
fig.tight_layout(pad=0)

# save the figure
fig.savefig('orig_gray_sepia.pdf')

plt.show()
