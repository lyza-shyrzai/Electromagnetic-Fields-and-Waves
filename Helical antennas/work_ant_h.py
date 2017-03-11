# Plot of working antenna in the H-plane
# Antenna parameters: 
# d(Coil diameter) = 10 mm, 
# S(distance between the coils) = 5 mm

import matplotlib.pyplot as plt
import numpy as np

angles = np.array([-90, -60, -40, 0, 72, 80, 90])
u = np.array     ([100, 1000, 150, 2000, 45, 85, 40])

plt.plot(angles, u)
plt.title("Plot of working antenna in the H-plane")
plt.text(-96, 1835, s="d(Coil diameter) = 10 mm \nS(distance between the coils) = 5 mm", bbox = {"boxstyle":"square", "facecolor":"w"})
plt.xlabel('angles')
plt.ylabel('u, µV')

plt.grid(True)
plt.savefig("work_ant_h.png")
plt.show()