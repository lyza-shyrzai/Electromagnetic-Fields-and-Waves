# Plot of E-sectorial antenna in the H-plane

import matplotlib.pyplot as plt
import numpy as np

angles = np.array([-90, -83, -60, 0, 50, 60, 90])
u = np.array([10, 45, 35, 9000, 500, 1000, 800])

plt.plot(angles, u)
plt.yscale('log')
plt.xlabel('angles')
plt.ylabel('u, µV')

plt.grid(True)
plt.savefig("e_h.png")
plt.show()