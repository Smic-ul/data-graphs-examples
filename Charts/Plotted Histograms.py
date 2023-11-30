import matplotlib.pyplot as plt
import numpy as np

mu, sigma = 172, 8
x = mu + sigma * np.random.randn(10000)

plt.hist(x, 200, facecolor='blue', density=True)
plt.xlabel('Heights')
plt.ylabel('Percentage of Students')
plt.title('Heights of Students')
plt.text(145, 0.04, "μ = 172, sig = 8")
plt.grid(True)
plt.show()
