 # -*- coding: utf-8 -*-
"""
Pipes, Filters & Classes

e.g., 
    p = Pipe(Reader('mydata.txt'), Trim(20), Head(10), Sort())
    results = p.run()
"""

import generate_data as gd
import numpy as np
np.set_printoptions(threshold=np.inf)



class Filter():
    """Base class that knows how to read and write data streams. Likely to end up as a queue of some sort"""
    def __init__(self, nrow=20, frequency=440, samplingrate=10, duration=1):
        self.datagen = []
        self.data = []
        self.nrow = nrow
        self.frequency = frequency
        self.samplingrate = samplingrate
        self.duration = duration
    
    def collect_data(self):
        data = gd.Generator(nrow=self.nrow, frequency=self.frequency, samplingrate=self.samplingrate, duration=self.duration)
        self.datagen = data.create_data()
        
        
class Reader(Filter):
    """Class that just produces output of Filter"""
    def __init__(self):
        Filter.__init__(self)
        Filter.collect_data(self)
        
    def run(self, *args):
        record = args[0]
        print(record)
        return record
     
class Trim(Filter):
    """For each line of input, Trim produces one line of output trimmed to given number of elements"""
    def __init__(self, ntrim=2):
        Filter.__init__(self)
        Filter.collect_data(self)
        self.ntrim = ntrim
        
    def run(self, *args):
        record = args[0]
        if record == 'EOF':
            return self.rtrim
        self.rtrim = record[:self.ntrim]
        print('\n Trim: \n', self.rtrim)            

class Head(Filter):
    """Echos the first lines of input unchanged, then stops producing output"""
    def __init__(self, nhead=5):
        Filter.__init__(self)
        Filter.collect_data(self) 
        self.nhead = nhead
        self.head = []
        
    def run(self, *args):
        record = args[0]
        index = args[1]
        if index < self.nhead:
            if index == 0:
                self.head = record
            else:
                self.head = np.vstack((self.head, record))
            print('\n Head: \n', record)    
        elif record == 'EOF':
            print('\n Head: \n', self.head)
            return self.head

    
class Sort(Filter):
    """Waits until it has read all of the input, then starts producing output"""
    def __init__(self):
        Filter.__init__(self)
        Filter.collect_data(self)
        
    def run(self, *args):
        record = args[0]
        index = args[1]            
        if index == 0:
            self.data = record
        elif record == 'EOF':
            print('\n Sort: \n', self.data)
            return self.data
        else:
            self.data = np.vstack((self.data, record))


       
    
class Pipe(Filter):
    """Given a bunch of objects, Pipe puts them in a list and starts running them
    e.g., 
        def run(self):
            while (there's still data to process):
                for filter in self.filter_list:
                filter.next_record()
        """
    def __init__(self, ntrim=2, nhead=5):
        Filter.__init__(self)
        Filter.collect_data(self)
        self.data = []
        self.record = []
        self.filter_list = []
        self.ntrim = ntrim
        self.nhead = nhead
        

    def get_filter_list(self):
        self.filter_list = Reader(), Trim(self.ntrim), Head(self.nhead), Sort()
        return self
        
    
    def run(self):
        Pipe.get_filter_list(self)
        index = 0
        for record in self.datagen:
            print('\n ----- Record ', index, ' -----')
            for filter in self.filter_list:
                self.data = filter.run(record, index)
            index += 1
        return self
            
            
        
        
        
    
        
        
        

