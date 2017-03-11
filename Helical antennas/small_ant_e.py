# Plot of smaller antenna in the E-plane
# Antenna parameters: 
# d(Coil diameter) = 5.5 mm, 
# S(distance between the coils) = 5 mm

import matplotlib.pyplot as plt
import numpy as np

angles = np.array([-49, -35, -20, 0, 20, 37, 90])
u = np.array     ([30, 550, 90, 1100, 40, 500, 160])

plt.plot(angles, u)
plt.title("Plot of smaller antenna in the E-plane")
plt.text(15, 1100, s="d(Coil diameter) = 5.5 mm \nS(distance between the coils) = 5 mm", bbox = {"boxstyle":"square", "facecolor":"w"})
plt.xlabel('angles')
plt.ylabel('u, µV')

plt.grid(True)
plt.savefig("small_ant_e.png")
plt.show()