import numpy as np
import matplotlib.pyplot as plt


labels = ["Apple", "Banana", "Cherry", "Dates"]
sizes = [25, 35, 20, 20]

plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=140)
plt.title("Pie Chart Example")
plt.show()
