import numpy as np
import matplotlib.pyplot as plt

# Define the length of the impulse response
N = 10

# Create the impulse response h(n) = δ(n) - δ(n+1)
h = np.zeros(N)
h[0] = 1  # δ(n)
h[1] = -1  # -δ(n+1)

# Plot the stem plot of the impulse response
plt.stem(range(N), h,linefmt='b-', markerfmt='bo', basefmt='r')
plt.xlabel('$n$')
plt.ylabel('$h(n)$')
plt.title('Filter Impulse Response')
plt.grid(True)
plt.savefig('h(n).png')

