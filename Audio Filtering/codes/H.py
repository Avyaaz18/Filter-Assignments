import numpy as np
import matplotlib.pyplot as plt

def H(z):
    num = np.polyval([0.01, 0.05, 0.05, 0.01], z**(-1))
    den = np.polyval([1, -2, 1], z**(-1))
    H = num / den
    return H

omega = np.linspace(-5*np.pi,5*np.pi,100)


plt.plot(omega, abs(H(np.exp(1j*omega))))
plt.title('Filter Frequency Response')
plt.xlabel('$\omega$')
plt.ylabel('$|H(e^{\jmath\omega})| $')
plt.grid()
plt.savefig('|H(z)|.png')
#plt.show()

