import numpy as np
from matplotlib import pyplot as plt

data = [1,0,0,0,0,0,0,0,0,0,1,1,0,1]
time = np.arange(len(data))
signal = np.zeros(len(data), dtype = int)
flg= False
i = 0
while i <len(data):
    if len(data) -i >=8:
        if data[i:i+8] == [0]*8:
            if flg:
                signal[i+3] = 1
                signal[i+4] = -1
                signal[i+6] = -1
                signal[i+7] = 1
            else:
                signal[i+3] = -1
                signal[i+4] = 1
                signal[i+6] = 1
                signal[i+7] = -1
                
            i+=8
            continue

    if data[i] == 1:
        if flg:
            signal[i] = -1
        else:
            signal[i] = 1
        flg = not flg
    else:
        signal[i] = 0
    i+=1
    

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
