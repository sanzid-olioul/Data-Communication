import numpy as np
from matplotlib import pyplot as plt

data = [int(x) for x in input().split()]
time = np.arange(len(data))
signal = np.zeros(len(data), dtype = int)
flg= False
for i in range(0,len(data)):
    if data[i] == 1:
        if flg:
            signal[i] = -1
        else:
            signal[i] = 1
        flg = not flg
    else:
        signal[i] = 0
    

plt.step(time, signal,where='post')
plt.title('AMI')
plt.xlabel('Amplitude')
plt.ylabel('Time')
plt.text(0, 2, data)

# plt.text(3, 8)
plt.grid(True)
plt.yticks([-2,-1,0,1,2,3])
plt.xticks(np.arange(len(data)))
plt.show()
