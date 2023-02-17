import numpy as np
from matplotlib import pyplot as plt

data = [int(x) for x in input().split()]
time = np.arange(len(data))
signal = np.zeros(len(data), dtype = int)
flg= False
eve = True
i = 0
while i <len(data):
    if len(data) -i >=4:
        if data[i:i+4] == [0]*4:
            if eve:
                if not flg:
                    signal[i] = 1
                    signal[i+3] = 1
                    flg = True
                else:
                    signal[i] = -1
                    signal[i+3] = -1
                    flg = False
            else:
                if not flg:
                    signal[i+3] = -1
                    flg = False
                else:
                    signal[i+3] = 1
                    flg = True
            i+=4
            eve = True
            
            continue

    if data[i] == 1:
        if flg:
            signal[i] = -1
        else:
            signal[i] = 1
        flg = not flg
        eve = not eve
    else:
        signal[i] = 0
    i+=1
    

plt.step(time, signal,where='post')
plt.title('HDB3')
plt.xlabel('Amplitude')
plt.ylabel('Time')
plt.text(0, 2, data)

# plt.text(3, 8)
plt.grid(True)
plt.yticks([-2,-1,0,1,2,3])
plt.xticks(np.arange(len(data)))
plt.show()
