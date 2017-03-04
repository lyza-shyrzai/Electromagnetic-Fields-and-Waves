# Plot of E-sectorial antenna in the E-plane

import matplotlib.pyplot as plt
import numpy as np

angles = np.array([-70, -50, -40, 0, 35, 55, 90])
u = np.array     ([5, 130, 10, 22000, 50, 150, 10])

plt.plot(angles, u)
plt.yscale('log')
plt.xlabel('angles')
plt.ylabel('u')

plt.grid(True)
plt.savefig("e_e.png")
plt.show()