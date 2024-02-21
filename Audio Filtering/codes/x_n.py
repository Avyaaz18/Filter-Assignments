import numpy as np
import matplotlib.pyplot as plt

x = np.array([0.174, 0.0415, 0.013, 0.10837, -0.00360])

plt.stem(range(len(x)), x, linefmt='b-', markerfmt='bo', basefmt='r')
plt.xlabel('$n$')
plt.ylabel('$x(n)$')
plt.grid(True)

# Set custom ticks for the x-axis
plt.xticks(range(len(x)))

plt.savefig('x(n).png')

