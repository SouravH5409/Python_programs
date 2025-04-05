import numpy as np
import matplotlib.pyplot as plt


categories = ['A', 'B', 'C', 'D']
values = [5, 7, 3, 8]

plt.figure(figsize=(8, 6))

# Vertical Bar Plot
plt.subplot(1, 2, 1)
plt.bar(categories, values, color='blue')
plt.title("Vertical Bar Plot")

# Horizontal Bar Plot
plt.subplot(1, 2, 2)
plt.barh(categories, values, color='green')
plt.title("Horizontal Bar Plot")

plt.tight_layout()
plt.show()
