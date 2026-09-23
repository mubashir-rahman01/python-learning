import matplotlib.pyplot as plt
import numpy as np

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x,y, 
     marker=".",
     markersize=12,
     markerfacecolor="b",
     markeredgecolor="b",
     linestyle="dotted",
     color="green"
    );

# Adding labels
plt.title("Smart Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burn")

plt.show()
