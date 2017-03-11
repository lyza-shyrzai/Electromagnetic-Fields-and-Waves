# Plot of smaller antenna in the H-plane
# Antenna parameters: 
# d(Coil diameter) = 5.5 mm, 
# S(distance between the coils) = 5 mm

import matplotlib.pyplot as plt
import numpy as np

angles = np.array([-90, -80, -25, 0, 32, 63, 70])
u = np.array     ([100, 300, 10, 500, 40, 1000, 800])

plt.plot(angles, u)
plt.title("Plot of smaller antenna in the H-plane")
plt.text(-95, 900, s="d(Coil diameter) = 5.5 mm \nS(distance between the coils) = 5 mm", bbox = {"boxstyle":"square", "facecolor":"w"})
plt.xlabel('angles')
plt.ylabel('u, µV')

plt.grid(True)
plt.savefig("small_ant_h.png")
plt.show()