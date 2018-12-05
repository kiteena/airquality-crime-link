
# coding: utf-8

# In[1]:

import numpy as np
import scipy as sp
import pydub
import matplotlib as plt 
from pyAudioAnalysis import audioTrainTest as aT


# In[2]:

# Reading the dataset with .wav files
#sr, x = scipy.io.wavfile.read('/home/sarvpsin/Desktop/pyAudioAnalysis/pyAudioAnalysis/Data_mic/gun_shot_wav/102305.wav ')


# In[8]:


aT.featureAndTrain(["/home/sarvpsin/Desktop/pyAudioAnalysis/pyAudioAnalysis/Data_mic/gun_shot_wav", "/home/sarvpsin/Desktop/pyAudioAnalysis/pyAudioAnalysis/Data_mic/car_horn_wav"], 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "svm", "SVMTry", False)


# In[12]:

#train test split here

aT.fileClassification("/home/sarvpsin/Desktop/pyAudioAnalysis/pyAudioAnalysis/Data_mic/Handgun_sound_effect_1-youtube-NWezpZms1VA-140-192.wav", "SVMTry","svm")


# In[6]:

# knn
#accuracy and F1_score


# In[7]:

#svm
#accuracy and F1_score


# In[8]:

#random forest
#accuracy and F1_score


# In[9]:

#CPU Usage


# In[ ]:

#Time taken by each model

