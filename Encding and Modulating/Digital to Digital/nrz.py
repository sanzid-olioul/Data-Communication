import numpy as np
from matplotlib import pyplot as plt

data = [int(x) for x in input().split()]
time = np.arange(len(data))
signal_i = np.zeros(len(data), dtype = int)
signal_l = np.zeros(len(data), dtype = int)
flg = True
for i in range(len(data)):
    if data[i] == 1:
        flg = not flg
    if flg:
        signal_i[i] = 1
    else:
        signal_i[i] = -1

plt.subplot(2, 1, 1)
plt.step(time, signal_i,where='post')
plt.title('NRZ-I')
plt.xlabel('Amplitude')
plt.ylabel('Time')
plt.text(0, 2, data)

# plt.text(3, 8)
plt.grid(True)
plt.yticks([-2,-1,0,1,2,3])
plt.xticks(time)




time = np.arange(len(data))
signal_l = np.zeros(len(data), dtype = int)
for i in range(len(data)):
    if data[i] == 0:
        signal_l[i] = -1
    else:
        signal_l[i] = 1
    
plt.subplot(2, 1,2)
plt.step(time, signal_l,where='post')
plt.title('NRZ-L')
plt.xlabel('Amplitude')
plt.ylabel('Time')
plt.text(0, 2, data)

# plt.text(3, 8)
plt.grid(True)
plt.yticks([-2,-1,0,1,2,3])
plt.xticks(time)
plt.tight_layout()
plt.show()





