import numpy as np
import matplotlib.pyplot as plt

#Generate random data for the hsitogram
data = np.random.randn(1000) 

plt.hist(data, bins=30, color="purple", edgecolor="black")
plt.title("Histogram Example")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
