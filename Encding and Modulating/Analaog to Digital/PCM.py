import numpy as np
import matplotlib.pyplot as plt
f = 10
t = np.linspace(0,1,1000)
y = np.sin(2 * np.pi *f * t)

samp_t = t[::35]
samp_y = y[::35]*127
samp_y = samp_y.astype(int)
val = []
for d in samp_y:
    if d <0:
        d = 256 + d
    print(d)
    val+=[int(x) for x in bin(d)[2:]]
print(val)

plt.subplot(3,1,1)
plt.plot(t,y)
plt.grid(True)
plt.subplot(3,1,2)
plt.stem(samp_t,samp_y)
plt.grid(True)

plt.subplot(3,1,3)
plt.step(np.arange(20), val[:20],where='post')
plt.title('Unipolar')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.text(0, 2, val[:20])
plt.grid(True)
plt.yticks([-2,-1,0,1,2,3])
plt.xticks(np.arange(20))
plt.tight_layout()
plt.show()


