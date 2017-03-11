# Plot of smaller antenna in the H-plane
# Antenna parameters: 
# d(Coil diameter) = 5.5 mm, 
# S(distance between the coils) = 5 mm

import matplotlib.pyplot as plt
import numpy as np

angles = np.array([-90, -50, -25, 0, 25, 49, 90])
u = np.array     ([100, 700, 500, 330, 125, 2000, 150])

plt.plot(angles, u)
plt.title("Plot of smaller antenna in the H-plane")
plt.text(-95, 1800, s="d(Coil diameter) = 5.5 mm \nS(distance between the coils) = 5 mm", bbox = {"boxstyle":"square", "facecolor":"w"})
plt.xlabel('angles')
plt.ylabel('u, µV')

plt.grid(True)
plt.savefig("small_ant_h.png")
plt.show()