
from cProfile import label
import matplotlib.pyplot as plt
import numpy as np


xData = np.array(["Kilojoules", "Fat", "Sugar", "Sodium"])


goalData = np.array([66.11, 66, 74, 23.00])

mondayData = np.array([43.36, 28, 12, 9.64])


tuesdayData = np.array([39.76, 18, 22, 9.17])

wednesdayData = np.array([22.15, 68, 32, 21.99])

thursdayData = np.array([31.71, 24, 34, 2.57])


plt.plot(xData, mondayData, marker='o', label="Monday", color="orange")
plt.plot(tuesdayData, marker='o', label="Tuesday", color="blue")
plt.plot(wednesdayData, marker='o', label="Wednesday", color="purple")
plt.plot(thursdayData, marker='o', label="Thursday", color="hotpink")


plt.ylabel("(g)")
plt.xlabel("(Nutrients)")
plt.plot(goalData, color='g', marker='o', mfc='r', label="Goal data")
plt.title("Week1")
plt.legend()
plt.grid()
plt.show()
