 # -*- coding: utf-8 -*-
"""
Pipes, Filters & Classes

e.g., 
    p = Pipe(Reader('mydata.txt'), Trim(20), Head(10), Sort())
    results = p.run()
"""

import numpy as np
import time

np.set_printoptions(threshold=np.inf)



class Filter():
    """Base class that knows how to read and write data streams. Likely to end up as a queue of some sort"""
    def __init__(self, text='haiku.txt'):
        self.datagen = []
        self.streaming = False
        self.record = []
    
    def collect_data(self):
        self.streaming = True
        self.datagen = self.create_data()
        
        
    def create_data(self):
        with open(self.text) as file:
            for line in file:
                time.sleep(.25)
                yield line    
        file.close()
                
        
        
class Reader(Filter):
    """Class that produces output of Filter. Returns single record.
    """
    def __init__(self, text='haiku.txt'):
        self.text = text
        self.record = []
        Filter.__init__(self)
        Filter.collect_data(self)
        
        
        
    def next_record(self, *args):
        self.record = args[0]
        print(self.record)
        return self.record

        
class Trim(Filter):
    """For each line of input, Trim produces one line of output trimmed to given number of elements"""
    def __init__(self, ntrim=5):
        Filter.__init__(self)
        Filter.collect_data(self)
        self.ntrim = ntrim
        self.trim = []
        
    def next_record(self, *args):
        record = args[0]
        if record == 'EOF':
            return
        self.trim = record[:self.ntrim]
        print(self.trim)  

        
class Head(Filter):
    """Echos the first n lines (default = 5) of input unchanged, then stops producing output"""
    def __init__(self, nhead=5):
        Filter.__init__(self)
        Filter.collect_data(self) 
        self.nhead = nhead

        
    def next_record(self, *args):
        record = args[0]
        index = args[1]
        if record == 'EOF':
            return
        if index < self.nhead:
            if index == 0:
                self.head = record
            else:
                self.head = np.vstack((self.head, record))
            print(record)    
        

    
class Sort(Filter):
    """Waits until it has read all of the input, then starts producing output"""
    def __init__(self):
        Filter.__init__(self)
        Filter.collect_data(self)
        
    def next_record(self, *args):
        record = args[0]
        index = args[1]            
        if index == 0:
            self.sort = record
        elif record == 'EOF':
            print(self.sort)
            return
        else:
            self.sort = np.vstack((self.sort, record))


       
    
class Pipe(Reader, Trim, Head, Sort):
    """Given a bunch of objects, Pipe puts them in a list and starts running them"""
    def __init__(self, *args):
        Reader.__init__(self)
        Trim.__init__(self)
        Head.__init__(self)
        Sort.__init__(self)
        self.record = []
        self.filter_list = []
        self.data = []
        
        if len(args) < 1:
            args = Reader(), Trim(), Head(), Sort()
        self.filter_list = args



        
    
    def run(self):
        """RUN runs the filters Reader, Trim, Head, and Sort and 
        outputs the results of the last input filter
        
        ## Parameters
        
        ### Input
        
        None
        
        ## Output
        
        data:  the output of the last filter run (default is Sort)  
        """
        while self.streaming == True:
            for index, record in enumerate(self.datagen):
                for filter in self.filter_list:
                    filter.next_record(record, index)
            self.streaming = False
            return
            
            
        
        
        
    
        
        
        

