# Plot of H-sectorial antenna in the H-plane

import matplotlib.pyplot as plt
import numpy as np

angles = np.array([-35, -22, -10, 0, 32, 45, 52])
u = np.array     ([25, 70, 10, 90, 5, 50, 20])

plt.plot(angles, u)
#plt.yscale('log')
plt.title("H-sectorial horn antenna in the H-plane")
plt.xlabel('angles')
plt.ylabel('u, µV')

plt.grid(True)
plt.savefig("h_h.png")
plt.show()