import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 10)
y = np.sin(x)

plt.stem(x, y)  #gives teh stem plot
plt.title("Stem Plot Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
