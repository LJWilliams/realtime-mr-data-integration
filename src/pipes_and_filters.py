# -*- coding: utf-8 -*-
"""
Pipes, Filters & Classes

e.g., 
    p = Pipe(Reader('mydata.txt'), Trim(20), Head(10), Sort())
    results = p.run()
"""

import time
import generate_data as gd



class Filter():
    """Base class that knows how to read and write data streams. Likely to end up as a queue of some sort"""
    def __init__(self, nrow=20, frequency=440, samplingrate=20, duration=1):
        self.newobs = []
        self.nrow = nrow
        self.frequency = frequency
        self.samplingrate = samplingrate
        self.duration = duration
    
    def collect_data(self):
        data = gd.Generator(nrow=self.nrow, frequency=self.frequency, samplingrate=self.samplingrate, duration=self.duration)
        for row in data.create_data():
            time.sleep(1)
            self.data = row
            return self.data
        
        
class Reader(Filter):
    """Class that just produces output of Filter"""
    def __init__(self):
        Filter.__init__(self, nrow=20, frequency=440, samplingrate=20, duration=1)
        Filter.collect_data(self)
        
    def print_output(self):
        print(self.data)
        
        
class Trim(Filter):
    """For each line of input, Trim produces one line of output trimmed to given number of elements"""
        
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

        

