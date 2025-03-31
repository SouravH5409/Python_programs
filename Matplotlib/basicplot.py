import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y1 = np.sin(x)  #for sine wave
y2 = np.cos(x)  #for cosine wave

plt.figure(figsize=(8, 6))
plt.plot(x, y1, label="Sine Wave")
plt.plot(x, y2, label="Cosine Wave", linestyle="dashed")
plt.title("Basic Line Plots")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid()
plt.show()
