# Plot of bigger antenna in the H-plane
# Antenna parameters: 
# d(Coil diameter) = 14 mm, 
# S(distance between the coils) = 8 mm

import matplotlib.pyplot as plt
import numpy as np

angles = np.array([-71, -39, -5, 0, 43, 85, 90])
u = np.array     ([200, 400, 150, 80, 200, 250, 150])

plt.plot(angles, u)
plt.title("Plot of bigger antenna in the H-plane")
plt.text(0, 355, s="d(Coil diameter) = 14 mm \nS(distance between the coils) = 8 mm", bbox = {"boxstyle":"square", "facecolor":"w"})
plt.xlabel('angles')
plt.ylabel('u, µV')

plt.grid(True)
plt.savefig("big_ant_h.png")
plt.show()