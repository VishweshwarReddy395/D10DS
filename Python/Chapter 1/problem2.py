# Installing a Random Module and Performing its Operations 

import matplotlib.pyplot as plt
import numpy as np

a=np.array([10,60,20,10])

plt.pie(a)

plt.show()

# Operation 2

import matplotlib.pyplot as plt

labels=['Ford','Ferrari','Nissan','Toyota','Porsche']
sizes=[10,15,30,20,25]
color=['Red','Yellow','Pink','blue']


plt.pie(sizes,labels=labels,colors=color)

plt.title("Popular Cars")

plt.show()


# Installing Another Module

import pyttsx3
engine = pyttsx3.init()

# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

engine.say("I will speak this text")
engine.runAndWait()