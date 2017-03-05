# Yagi antenna radiation pattern without directors with the signal from the receiver training
import matplotlib.pyplot as plt
import numpy as np


theta = np.array([195, 50])
theta = np.radians(theta)
radii = np.array([5, 1.5])

ax = plt.subplot(111, projection='polar')
bars = ax.bar(theta, radii, bottom=0.0)

# Use custom colors and opacity
for r, bar in zip(radii, bars):
    bar.set_facecolor(plt.cm.viridis(r / 10.))
    bar.set_alpha(0.5)

plt.title("Radiation pattern without directors with the signal from the receiver training")
plt.savefig("without_dir_rec.png")
plt.show()
