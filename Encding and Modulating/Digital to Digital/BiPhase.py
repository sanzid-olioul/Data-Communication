import numpy as np
from matplotlib import pyplot as plt

data = [int(x) for x in input().split()]
time_org = np.arange(len(data))
signal_manch = np.zeros(len(data)*2, dtype = int)
signal_diff = np.zeros(len(data)*2, dtype = int)

for i in range(0,len(data)*2,2):
    if data[i//2] == 0:
        signal_manch[i] = 1
        signal_manch[i+1] = -1
    else:
        signal_manch[i] = -1
        signal_manch[i+1] = 1


print(signal_manch)
time = np.arange(len(signal_manch))
plt.subplot(2, 1, 1)
plt.step(time, signal_manch,where='post')
plt.title('Manchestor')
plt.xlabel('Amplitude')
plt.ylabel('Time')
plt.text(0, 2, data)

plt.grid(True)
plt.yticks([-2,-1,0,1,2,3])
plt.xticks(time_org*2)





start = False
for i in range(0,len(data)*2,2):
    if start:
        if data[i//2] == 0:
            signal_diff[i] =  -1*signal_diff[i-1]
            signal_diff[i+1] = signal_diff[i-1]
        else:
            signal_diff[i] = signal_diff[i-1]
            signal_diff[i+1] = -1* signal_diff[i-1]
    else:
        start = True
        if data[i//2] == 0:
            signal_diff[i] = -1
            signal_diff[i+1] = 1
        else:
            signal_diff[i] = 1
            signal_diff[i+1] = -1


print(signal_diff)
time = np.arange(len(signal_diff))
plt.subplot(2, 1, 2)
plt.step(time, signal_diff,where='post')
plt.title('Differential Manchestor')
plt.xlabel('Amplitude')
plt.ylabel('Time')
plt.text(0, 2, data)

plt.grid(True)
plt.yticks([-2,-1,0,1,2,3])
plt.xticks(time_org*2)
plt.tight_layout()
plt.show()





