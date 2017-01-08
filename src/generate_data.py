#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 21:38:30 2017

@author: alw
"""
import numpy as np

class Generator():
    def __init__(self, nrow=20, frequency=440, samplingrate=20, duration=1):
        """Sets up the parameters for generating a series of sine waves as a sample data set
        
        ##Parameters
        - nrow:         the number of rows to create in the data set
        - frequency:    frequency of sine wave (default 440 Hz)
        - samplingrate: the sampling rate in Hz of the sine wave (default 20 Hz)
        - duration:     the duration of the sample in seconds (default 1 second)
        """
        self.nrow = nrow
        self.frequency = frequency*1.0 # must be float
        self.samplingrate = samplingrate
        self.duration = duration*1.0 # must be float

    def create_data(self):
        index = 1
        while index <= self.nrow:
            index += 1
            newobs = (np.sin(index*np.pi*np.arange(self.samplingrate*self.duration)*self.frequency/self.samplingrate)).astype(np.float32)
            yield newobs