 # -*- coding: utf-8 -*-
"""
Pipes, Filters & Classes

e.g., 
    p = Pipe(Reader('mydata.txt'), Trim(20), Head(10), Sort())
    results = p.run()
"""


import time

class Filter():
    """Base class that knows how to read and write data streams. Likely to end up as a queue of some sort"""
    def __init__(self):
        #if len(args) >= 1 and type(args[0] == str):
        #    self.text = args[0]
        print(self.text)
            
        self.datagen = []
        self.data = []
        self.streaming = True
        self.record = []
        self.index = []
        self.file = []
        self.title = 'Filter'
        
        
    def __iter__(self):
        return(self)
                
    def __eq__(self, other):
        return self.title == other.title
        
    def next(self):
        print(self.text)
        with open(self.text) as self.file:
            for line in self.file:
                return line
        
        
        
      # To come soon!

      
class Reader(Filter):
    """Class that produces output of Filter. Returns single record.
    """
    def __init__(self, text='haiku.txt'):
        self.record = []
        self.text = text
        self.title = 'Reader'
        
    def __eq__(self, other):
        return self.title == other.title
        
    def next_record(self):
        self.gen = Filter()
        self.record = self.gen.next()
        print(self.record)
        return self
       

  
            

        
        
    
        
        
        

