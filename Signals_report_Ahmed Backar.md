





**Signals Report**

MileStone 1

Team:

- Ahmed Backar        55-24857        T-26



**Description:**

In this milestone I have created a sound from 2 sets of frequency list where one list is from the 3<sup>rd</sup> octave of piano frequency sets and the other is from the 4<sup>th</sup> octave of piano frequency set, then I added the 2 lists on each other with their respective time frame to create one sound lasting 3 seconds.

**Steps:**

(1). We started with defining the time for which the song will be playing for . and how many samples are in them. The time limit was set to 3 seconds and 3\*1024 samples.   #t= np.linspace(0,3,12\*1024)

(2)We then defined the 2 frequency sets from the 3<sup>rd</sup> and 4<sup>th</sup> octave.

\# Fi\_1=np.array([130.81,220,0,246.93,164.81] 

#Fi\_2=np.array([440,392,293.66,0,0])

(3) We then defined a list for each pair to define when each frequency will be played and for how long it will be

\# played.Start=np.array([0,0.9,1.7,2.3,2.7])

#periods=np.array([0.9,0.6,0.5,0.3,0.3])

(4)We then looped on the frequency Lists adding all the frequency pairs at their correct start and their correct period and we changed frequency into a sine signal.

#count=0

#sumNotes=0

#while(count<5):

\#    oct\_3=Fi\_1[count]

\#  oct\_4=fi\_2[count]

\#  Note1=np.sin(2\*np.pi\*oct\_3\*t)

\# Note2=np.sin(2\*np.pi\*oct\_4\*t)

\#  S=Start[count]

\#  Tp=periods[count]

\#   sumNotes=sumNotes+((Note1+Note2)\*((t>=S)&(t<=(S+Tp))))

\#    count=count+1

(5)we then plotted the summed sounds and plotted them on a time graph producing the following graph.








**Signals Report**

MileStone 2

Team:

- Ahmed Backar        55-24857        T-26



**Description:**

In this milestone I have created a random noise from 2 random frequencies and I added them to the sound from milestone 1 which I then cancelled them returning our signal to its original form.

**Steps:**

(1)We set N to our sample from milestone 1 and set a frequency list from 0 to 512 with half the numbers of our samples in our time list.

#N=3\*1024

#f= np.linspace(0, 512, int(N/2))

(2)We then turned our original signal from a time domain into the frequency domain using the function provided to us on the milestone description and then plotted it. Which produced this graph.

\# plt.figure()

\# SF= fft(sumNotes) 

\# SF = 2/N \* np.abs(SF [0:int(N/2)])

\# plt.plot(f, SF)

\# 



(3) we then produced 2 random frequencies for our noise

\# fn1 , fn2= np.random.randint(0,512,2)

(4)we then added the 2 random frequencies to our original sound making them sin signals and plotted the graph giving us the signal with noise .

\# NSN= sumNotes +  np.sin(2\*np.pi\*fn1\*t)+np.sin(2\*np.pi\*fn2\*t)

\# plt.figure()

\# plt.plot(t,NSN)

(5)We then turned the sound with noise from time domain into frequency domain and plotted its frequency graph producing this graph.

#NSF= fft(NSN)

#NSF = 2/N \* np.abs(NSF [0:int(N/2)])

#plt.figure()

#plt. plot(f,NSF) 

(6)from the frequency graph I found that we can get the indices of the 2 random frequencies if we compare the original sound frequency graph with the one with noise. And getting the 2 highest frequencies as the random frequencies produced the highest frequency. I then retracted the random frequencies using the indexes on the frequency list.

#LBF=np.where(NSF> math.ceil(np.max(SF)))

#i1= LBF[0][0]

#i2= LBF[0][1]

#freq1=int(f[i1])

#freq2=int(f[i2])

(7)we then removed the 2 frequencies from the sound containing the noise frequencies and plotted the graph with the removed frequencies which produced the Graph of the original sound therefore producing the wanted sound and NCA.

#x\_fil= NSN-(np.sin(2\*np.pi\*freq1\*t)+np.sin(2\*np.pi\*freq2\*t))

#plt.figure()

#plt.plot(t,x\_fil)


(8I finally turned the sound with removed frequency into frequency domain and plotted it

#x\_Freq\_fil=fft(x\_fil)

#x\_Freq\_fil = 2/N \* np.abs(x\_Freq\_fil [0:int(N/2)])

#plt.figure()

\# plt.plot(f,x\_Freq\_fil)

**GRAPHS:**
**



**












**Code:**

**import numpy as np**

**import matplotlib.pyplot as plt**

**import sounddevice as sd**

**from scipy.fftpack import fft**

**import math**


**t= np.linspace(0,3,12\*1024)**

**Fi\_1=np.array([130.81,220,0,246.93,164.81])**

**#note frequencies(C3,A3,No,B3,E3)**

**fi\_2=np.array([440,392,293.66,0,0])**

**#note frequencies(A4,G4,D4,No,No)**

**Start=np.array([0,0.9,1.7,2.3,2.7])**

**periods=np.array([0.9,0.6,0.5,0.3,0.3])**


**count=0**

**sumNotes=0**

**while(count<5):**

`    `**oct\_3=Fi\_1[count]**

`    `**oct\_4=fi\_2[count]**

`    `**Note1=np.sin(2\*np.pi\*oct\_3\*t)**

`    `**Note2=np.sin(2\*np.pi\*oct\_4\*t)**

`    `**S=Start[count]**

`    `**Tp=periods[count]**

`    `**sumNotes=sumNotes+((Note1+Note2)\*((t>=S)&(t<=(S+Tp))))**

`    `**count=count+1**

**plt.figure()**

**plt.plot(t, sumNotes)**

**N=3\*1024**

**f= np.linspace(0, 512, int(N/2))**

**plt.figure()**

**SF= fft(sumNotes)**

**SF = 2/N \* np.abs(SF [0:int(N/2)])**

**plt.plot(f, SF)**

**fn1 , fn2= np.random.randint(0,512,2)**

**NSN= sumNotes +  np.sin(2\*np.pi\*fn1\*t)+np.sin(2\*np.pi\*fn2\*t)**

**plt.figure()**

**plt.plot(t,NSN)**

**NSF= fft(NSN)**

**NSF = 2/N \* np.abs(NSF [0:int(N/2)])**

**plt.figure()**

**plt.plot(f,NSF)**

**LBF=np.where(NSF> math.ceil(np.max(SF)))**

**i1= LBF[0][0]**

**i2= LBF[0][1]**

**freq1=int(f[i1])**

**freq2=int(f[i2])**

**x\_fil= NSN-(np.sin(2\*np.pi\*freq1\*t)+np.sin(2\*np.pi\*freq2\*t))**

**plt.figure()**

**plt.plot(t,x\_fil)**

**x\_Freq\_fil=fft(x\_fil)**

**x\_Freq\_fil = 2/N \* np.abs(x\_Freq\_fil [0:int(N/2)])**

**plt.figure()**



