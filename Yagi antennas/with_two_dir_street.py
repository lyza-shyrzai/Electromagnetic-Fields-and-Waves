# Yagi antenna radiation pattern with two directors with interference from the street
import matplotlib.pyplot as plt
import numpy as np


theta = np.array([320, 295])
theta = np.radians(theta)
radii = np.array([8, 2.5])

ax = plt.subplot(111, projection='polar')
bars = ax.bar(theta, radii, bottom=0.0)

# Use custom colors and opacity
for r, bar in zip(radii, bars):
    bar.set_facecolor(plt.cm.viridis(r / 10.))
    bar.set_alpha(0.5)

plt.title("Radiation pattern with two directors with interference from the street")
plt.savefig("with_two_dir_street.png")
plt.show()
