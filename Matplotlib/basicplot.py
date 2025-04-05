import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.figure(figsize=(8, 6))
plt.plot(x, y1, label="Sine Wave")
plt.plot(x, y2, label="Cosine Wave", linestyle="dashed")
plt.title("Basic Line Plots")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid()
plt.show()
