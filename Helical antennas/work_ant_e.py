# Plot of working antenna in the E-plane
# Antenna parameters: 
# d(Coil diameter) = 10 mm, 
# S(distance between the coils) = 5 mm

import matplotlib.pyplot as plt
import numpy as np

angles = np.array([-70, -60, -40, 0, 39, 45, 55])
u = np.array     ([80, 180, 50, 2000, 400, 550, 400])

plt.plot(angles, u)
plt.title("Plot of working antenna in the E-plane")
plt.text(-78, 1835, s="d(Coil diameter) = 10 mm \nS(distance between the coils) = 5 mm", bbox = {"boxstyle":"square", "facecolor":"w"})
plt.xlabel('angles')
plt.ylabel('u, µV')

plt.grid(True)
plt.savefig("work_ant_e.png")
plt.show()