import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100) 
y = np.sin(x) 

plt.plot(x, y)
plt.title("Sine Wave")
plt.xlabel("X-axis")
plt.ylabel("sin(x)")
plt.grid()
plt.show()
