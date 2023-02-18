import numpy as np
import matplotlib.pyplot as plt
f = int(input())
t = np.linspace(0,1,2000)
y1 = np.sin(2 * np.pi *4*f * t)
y2 = np.sin(2 * np.pi *f * t)

temp = 0
b=[]
for i in range(temp,len(t),250):
    b.append(t[i])

b.append(1000)


v=[]
sft = True
for i in range(len(t)):
    if b[0]==t[i]:
        print(i)
        b.pop(0)
        sft = not sft
    if sft:
        v.append(np.sin(2*np.pi*4*f*t[i]))
    else:
        v.append(np.sin(2*np.pi*4*f*t[i])*-1)


plt.subplot(3,1,1)
plt.plot(t,y1)
plt.xlabel("time")
plt.ylabel("Amplitude")
plt.title("Carrier")
plt.grid(True)
plt.subplot(3,1,2)
plt.plot(t,y2)
plt.xlabel("time")
plt.ylabel("Amplitude")
plt.title("Modulating")
plt.grid(True)


plt.subplot(3,1,3)
plt.plot(t,v)
plt.xlabel("t")
plt.ylabel("Amplitude")
plt.title("PM")
plt.grid(True)
plt.tight_layout()
plt.show()
