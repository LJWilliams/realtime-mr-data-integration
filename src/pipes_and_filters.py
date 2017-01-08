# -*- coding: utf-8 -*-
"""
Pipes, Filters & Classes

e.g., 
    p = Pipe(Reader('mydata.txt'), Trim(20), Head(10), Sort())
    results = p.run()
"""

import numpy as np


class Filter():
    """Base class that knows how to read and write data streams"""
    def get_sine(index=2, f=440.0, fs=40, duration=1.0):
        """Generate a sine wave (requires numpy as np)
        ------------
        PARAMETERS
        ------------
        index = ???
        f = frequncy in Hz (must be float)
        fs = sampling rate in Hz (must be float)
        duration = duration in seconds
        
        ------------
        USAGE
        ------------
        get_sine(index, f, fs, duration)
        """
        sine = (np.sin(index*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32)
        return sine
    
      
    def get_data(nrow=10):
        index = 1
        while index <= nrow:
            index += 1
            newobs = Filter.get_sine(index=index)
            yield newobs

        
class Reader(Filter):
    """Class that just produces output"""
    for row in Filter.get_data():
        print(row)
        
class Trim(Filter):
    """For each line of input, Trim produces one line of output"""
        
class Head(Filter):
    """Echos the first lines of input unchanged, then stops producing output"""
        
class Sort(Filter):
    """Waits until it has read all of the input, then starts producing output"""
        
class Pipe(Filter):
    """Given a bunch of objects, Pipe puts them in a list and starts running them
    e.g., 
        def run(self):
            while (there's still data to process):
                for filter in self.filter_list:
                filter.next_record()
        """

        
Reader
