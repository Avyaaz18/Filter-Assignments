import numpy as np
import matplotlib.pyplot as plt

x = np.array([0.174, 0.0415, 0.013, 0.10837, -0.00360])

k = 20
y = np.zeros(20)

y[0] = 0.01 * x[0]
y[1] = 0.01 * x[1] + 0.05 * x[0] + 2 * y[0]
y[2] = 0.01 * x[2] + 0.05 * x[1] + 0.05 * x[0] + 2 * y[1] + y[0]

for n in range(3, k - 1):
    if n < 5:
        y[n] = 0.01 * x[n] + 0.05 * x[n - 1] + 0.05 * x[n - 2] + 0.01 * x[n - 3] + 2 * y[n - 1] - y[n - 2]
    elif n > 4 and n < 6:
        y[n] = 0.05 * x[n - 1] + 0.05 * x[n - 2] + 0.01 * x[n - 3] + 2 * y[n - 1] - y[n - 2]
    elif n > 5 and n < 7:
        y[n] = 0.05 * x[n - 2] + 0.01 * x[n - 3] + 2 * y[n - 1] - y[n - 2]
    elif n > 6 and n < 8:
        y[n] = 0.01 * x[n - 3] + 2 * y[n - 1] - y[n - 2]
    else:
        y[n] = 2 * y[n - 1] - y[n - 2]

#print(y)
plt.stem(range(len(y)), y, linefmt='b-', markerfmt='bo', basefmt='r')
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
#plt.title('Stem Plot of $y(n)$')
plt.grid(True)
plt.savefig('y(n).png')

