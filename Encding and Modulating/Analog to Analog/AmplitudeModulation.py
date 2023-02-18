import numpy as np
import matplotlib.pyplot as plt

A_c = int(input())
f_c = int(input())
A_m = int(input())
f_m = int(input())


t = np.linspace(0, 1, 1000)

carrier = A_c*np.sin(2*np.pi*f_c*t)
modulator = A_m*np.sin(2*np.pi*f_m*t)
product = A_c*(1+np.sin(2*np.pi*f_m*t))*np.sin(2*np.pi*f_c*t)

plt.subplot(3,1,1)
plt.title('Amplitude Modulation')
plt.plot(modulator)
plt.ylabel('Amplitude')
plt.xlabel('Message signal')

plt.subplot(3,1,2)
plt.plot(carrier)
plt.ylabel('Amplitude')
plt.xlabel('Carrier signal')

plt.subplot(3,1,3)
plt.plot(product)
plt.ylabel('Amplitude')
plt.xlabel('AM signal')

plt.subplots_adjust(hspace=1)
plt.show()
