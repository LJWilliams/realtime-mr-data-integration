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
        self.datagen = []
        self.data = []
        self.streaming = True
        self.record = []
        self.index = []
        self.file = []
        self.title = 'Filter'
        
        
    def __iter__(self):
        with open(self.text) as self.file:
            for line in self.file:
                time.sleep(.25)
                yield line
                
    def __eq__(self, other):
        return self.title == other.title
                
    def stop_stream(self, streaming=False):
        for filter in self.filter_list:
            if filter != Sort():
                data = 'Only data from Sort() saved to output'
            else:
                data = self.retrieve_data(filter, streaming)
        return self, data
        
    def retrieve_data(self, filter, streaming):
        if filter == Sort():
            data = filter.next_record(streaming)
            data = list(data)
            data.pop(0)
            # save to sql database
            return self, data
        else:
            return
        
      # To come soon!

      
class Reader(Filter):
    """Class that produces output of Filter. Returns single record.
    """
    def __init__(self, text='haiku.txt'):
        Filter.__init__(self)
        self.record = []
        self.text = text
        self.title = 'Reader'
        
    def __eq__(self, other):
        return self.title == other.title
        
    def next_record(self, *args):
        self.streaming = args[0]
        if self.streaming == False:
            return self, self.record
        else:
            self.record = args[1]
            #print(self.record)

  
            
class Trim(Filter):
    """For each line of input, Trim produces one line of output trimmed to given number of elements"""
    def __init__(self, ntrim=5):
        Filter.__init__(self)
        self.ntrim = ntrim
        self.trim = []
        self.title = 'Trim'

        
    def __eq__(self, other):
        return self.title == other.title
        
        
    def next_record(self, *args):
        self.streaming = args[0]
        if self.streaming == False:
            return self, self.trim
        else:
            record = args[1]
            self.trim = record[:self.ntrim]
           # print(self.title)
            print(self.trim)  

  
            
class Head(Filter):
    """Echos the first n lines (default = 5) of input unchanged, then stops producing output"""
    def __init__(self, nhead=5):
        Filter.__init__(self)
        self.nhead = nhead
        self.head = []
        self.title = 'Head'

    def __eq__(self, other):
        return self.title == other.title
        
    def next_record(self, *args):
        self.streaming = args[0]
        if self.streaming == False:
            return self, self.head
        else:
            record = args[1]
            index = args[2]
            type(index)
            if index < self.nhead:
                self.head.append(record)
                #print(self.title)
                print(record)    

                
                
    
class Sort(Filter):
    """Waits until it has read all of the input, then starts producing output"""
    def __init__(self):
        Filter.__init__(self)
        self.sort = []
        self.title = 'Sort'

    def __eq__(self, other):
        return self.title == other.title
        
    def next_record(self, *args):
        streaming = args[0]
        if streaming == False:
            #print(self.title)
            print(*self.sort,sep='\n')
            return self, self.sort
        else:
            record = args[1]   
            self.sort.append(record)
        
        
             
    
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
        if len(args) <= 1:
            args = Reader(), Trim(), Head(), Sort()
        self.filter_list = args
        self.title = 'Pipe'

    def __eq__(self, other):
        return self.title == other.title
        
    
    def run(self):
        """RUN runs the filters Reader, Trim, Head, and Sort and 
        outputs the results of the last input filter
        
        data:  the output of the last filter run (default is Sort)  
        """
        streaming = self.streaming
        while streaming == True:
            for index, record in enumerate(self.filter_list[0]):
                for filter in self.filter_list:
                    filter.next_record(streaming, record, index)
            streaming = False
        else:
            self.stop_stream(streaming)
        return self
            
            
        
        
        
    
        
        
        

