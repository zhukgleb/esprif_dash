import matplotlib.pyplot as plt
import numpy as np
import random
import time


for i in range(0, 100):
    x = np.linspace(0, 2 * np.pi, 100)

    # Calculate the sine of each x value
    y = np.sin(x)

    # Create the plot
    plt.plot(x, y)

    # Add labels and title
    plt.xlabel("Angle (radians)")
    plt.ylabel("sin(x)")
    plt.title(str(random.randint(1, 10)))
    plt.savefig("temp.jpg")
    print("new")
