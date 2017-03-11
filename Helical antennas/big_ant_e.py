# Plot of bigger antenna in the E-plane
# Antenna parameters: 
# d(Coil diameter) = 14 mm, 
# S(distance between the coils) = 8 mm

import matplotlib.pyplot as plt
import numpy as np

angles = np.array([-90, -80, -25, 0, 32, 63, 70])
u = np.array     ([100, 300, 10, 500, 40, 1000, 800])

plt.plot(angles, u)
plt.title("Plot of bigger antenna in the E-plane")
plt.text(-95, 900, s="d(Coil diameter) = 14 mm \nS(distance between the coils) = 8 mm", bbox = {"boxstyle":"square", "facecolor":"w"})
plt.xlabel('angles')
plt.ylabel('u, µV')

plt.grid(True)
plt.savefig("big_ant_e.png")
plt.show()