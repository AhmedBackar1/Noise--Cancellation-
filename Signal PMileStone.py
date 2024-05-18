import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
from scipy.fftpack import fft
import math



t= np.linspace(0,3,12*1024)

Fi_1=np.array([130.81,220,0,246.93,164.81])
#note frequencies(C3,A3,No,B3,E3)
fi_2=np.array([440,392,293.66,0,0])
#note frequencies(A4,G4,D4,No,No)

Start=np.array([0,0.9,1.7,2.3,2.7])
periods=np.array([0.9,0.6,0.5,0.3,0.3])


count=0
sumNotes=0
while(count<5):
    oct_3=Fi_1[count]
    oct_4=fi_2[count]
    Note1=np.sin(2*np.pi*oct_3*t)
    Note2=np.sin(2*np.pi*oct_4*t)
    S=Start[count]
    Tp=periods[count]
    sumNotes=sumNotes+((Note1+Note2)*((t>=S)&(t<=(S+Tp))))
    count=count+1

plt.figure()
plt.plot(t, sumNotes)
sd.play(sumNotes,4*1024)
N=3*1024
f= np.linspace(0, 512, int(N/2))

plt.figure()
SF= fft(sumNotes)
SF = 2/N * np.abs(SF [0:int(N/2)])
plt.plot(f, SF)

fn1 , fn2= np.random.randint(0,512,2)

NSN= sumNotes +  np.sin(2*np.pi*fn1*t)+np.sin(2*np.pi*fn2*t)
plt.figure()
plt.plot(t,NSN)

NSF= fft(NSN)
NSF = 2/N * np.abs(NSF [0:int(N/2)])
plt.figure()
plt.plot(f,NSF)

LBF=np.where(NSF> math.ceil(np.max(SF)))
i1= LBF[0][0]
i2= LBF[0][1]

freq1=int(f[i1])
freq2=int(f[i2])

x_fil= NSN-(np.sin(2*np.pi*freq1*t)+np.sin(2*np.pi*freq2*t))
plt.figure()
plt.plot(t,x_fil)

x_Freq_fil=fft(x_fil)
x_Freq_fil = 2/N * np.abs(x_Freq_fil [0:int(N/2)])

plt.figure()
plt.plot(f,x_Freq_fil)














