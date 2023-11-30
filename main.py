import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style


# Used style from matplotlib.org
style.use('ggplot')

# Base values:
x = np.arange(-100, 101, 1)
y1 = 0.5 * x ** 2 + 2 * x
y2 = np.sin(x)

# Basic plots:
# plt.plot(x, y1, 'r--')
# plt.plot(x, y2, 'go')

# Subplots - Multiple windows:
plt.suptitle("All functions")
plt.figure(1)
ax1 = plt.subplot(221)
ax2 = plt.subplot(222)
ax3 = plt.subplot(223)
ax4 = plt.subplot(224)

plt.title("Sin Function")
plt.xlabel("X label")
plt.ylabel("Y label")

ax1.plot(x, y1)
ax2.plot(x, y2)
ax3.plot(x, y1, 'r')
ax4.plot(x, y2, 'g', label="sin")
plt.legend(loc='upper left')

plt.tight_layout()
plt.show()

