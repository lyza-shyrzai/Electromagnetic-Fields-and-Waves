# Yagi antenna radiation pattern without Directors with interference from the street
import matplotlib.pyplot as plt
import numpy as np


theta = np.array([325, 235])
theta = np.radians(theta)
radii = np.array([6.5, 4])

ax = plt.subplot(111, projection='polar')
bars = ax.bar(theta, radii, bottom=0.0)

# Use custom colors and opacity
for r, bar in zip(radii, bars):
    bar.set_facecolor(plt.cm.viridis(r / 10.))
    bar.set_alpha(0.5)

plt.title("Radiation pattern without directors with interference from the street")
plt.savefig("without_dir_street.png")
plt.show()
