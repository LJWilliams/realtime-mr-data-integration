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
    def __init__(self):
        self.datagen = []
        self.streaming = True
        self.record = []
        self.index = []
    
   # To come soon!
                
        
        
class Reader(Filter):
    """Class that produces output of Filter. Returns single record.
    """
    def __init__(self, text):
        Filter.__init__(self)
        self.file = text
        self.record = []
        
        
    def __iter__(self):
        with open(self.file) as file:
            for line in file:
                time.sleep(.25)
                self.record = line
                yield self.record
         
    def next_record(self, *args):
        print(self.record)
        return self.record

        
class Trim(Filter):
    """For each line of input, Trim produces one line of output trimmed to given number of elements"""
    def __init__(self, ntrim=5):
        Filter.__init__(self)
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


       
    
class Pipe(Filter):
    """Given a bunch of objects, Pipe puts them in a list and starts running them"""
    def __init__(self, *args):
        if not isinstance(args[0], Reader):
            arg = Reader()
            arg.append(args)
        Filter.__init__(self)
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
            for index, record in enumerate(self.filter_list[0]):
                for filter in self.filter_list:
                    filter.next_record(record, index)
            self.streaming = False
            return
            
            
        
        
        
    
        
        
        

