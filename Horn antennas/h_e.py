# Plot of H-sectorial antenna in the E-plane

import matplotlib.pyplot as plt
import numpy as np

angles = np.array([-85, -60, -42, 0, 40, 53, 85])
u = np.array     ([15, 150, 100, 300, 100, 130, 60])

plt.plot(angles, u)
#plt.yscale('log')
plt.title("H-sectorial horn antenna in the E-plane")
plt.xlabel('angles')
plt.ylabel('u, µV')

plt.grid(True)
plt.savefig("h_e.png")
plt.show()