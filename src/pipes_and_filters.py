 # -*- coding: utf-8 -*-
"""
Pipes, Filters & Classes

e.g., 
    p = Pipe(Reader('mydata.txt'), Trim(20), Head(10), Sort())
    results = p.run()
"""

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
    def __init__(self, text='haiku.txt'):
        Filter.__init__(self)
        self.file = []
        self.record = []
        self.text = text
        
        
    def __iter__(self):
        with open(self.text) as self.file:
            for line in self.file:
                time.sleep(.25)
                yield line
         
    def next_record(self, *args):
        self.streaming = args[0]
        if self.streaming == False:
            self.file.close()
            return self
        else:
            self.record = args[1]
            print(self.record)

  
            
class Trim(Filter):
    """For each line of input, Trim produces one line of output trimmed to given number of elements"""
    def __init__(self, ntrim=5):
        Filter.__init__(self)
        self.ntrim = ntrim
        self.trim = []
        
    def next_record(self, *args):
        self.streaming = args[0]
        if self.streaming == False:
            return self
        else:
            record = args[1]
            self.trim = record[:self.ntrim]
            print(self.trim)  

  
            
class Head(Filter):
    """Echos the first n lines (default = 5) of input unchanged, then stops producing output"""
    def __init__(self, nhead=5):
        Filter.__init__(self)
        self.nhead = nhead
        self.head = []

        
    def next_record(self, *args):
        self.streaming = args[0]
        if self.streaming == False:
            return self
        else:
            record = args[1]
            index = args[2]
            type(index)
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
        self.sort = []
        
    def next_record(self, *args):
        self.streaming = args[0]
        if self.streaming == False:
            print(*self.sort,sep='\n')
            return self
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
            self.streaming == False
        else:
            for filter in self.filter_list:
                filter.next_record(streaming, record, index)
        return self
            
            
        
        
        
    
        
        
        

