 # -*- coding: utf-8 -*-
"""
Pipes, Filters & Classes

e.g., 
    p = Pipe(Reader('mydata.txt'), Trim(20), Head(10), Sort())
    results = p.run()
"""


class Filter():
    """Base class that knows how to read and write data streams.
    Likely to end up as a queue of some sort.
    """

    def __init__(self):
        """Construct common elements of all filters."""
        self.title = 'Filter' # This one, I can guess... :-)

      
      # To come soon!

      
class Reader(Filter):
    """Class that produces output of Filter. Returns single record.
    """

    def __init__(self, filename='haiku.txt'):
        Filter.__init__(self) 
        self.title = 'Reader' # Good - override the default setting in the parent.
        self.file = open(filename)
        
    def __iter__(self):
        return self
    
    def __eq__(self, other):
        return self.title == other.title
        
          
    def next_record(self, record): # record defined here to keep same formatting for all next_record calls for all the filters. Is there a better way to do this?
        for record in self.file:
            return record
        

class Trim(Filter):
    """For each line of input, Trim produces one line of output trimmed to given number of elements"""
    def __init__(self, ntrim=5):
        Filter.__init__(self)
        self.ntrim = ntrim
        self.title = 'Trim'
 
    def __eq__(self, other):
        return self.title == other.title
          
    def next_record(self, record):
        if record == None:
            return
        trim = record[:self.ntrim]
        return trim
  
            
class Head(Filter):
    """Echos the first n lines (default = 5) of input unchanged, then stops producing output"""
    def __init__(self, nhead=5):
        Filter.__init__(self)
        self.nhead = nhead
        self.title = 'Head'
        self.index = 0

    def __eq__(self, other):
        return self.title == other.title

    def __iter__(self):
        return self
        
    def next_record(self, record):
        if self.index <= self.nhead and record != None:
            self.index +=1
            return record 
        else:
            return
                
                
    
class Sort(Filter):
    """Waits until it has read all of the input, then starts producing output"""
    def __init__(self):
        Filter.__init__(self)
        self.sort = []
        self.title = 'Sort'

    def __eq__(self, other):
        return self.title == other.title
        
    def next_record(self, record):
        if record == None:
            return self.sort
        else:
            self.sort.append(record)
            return
        
    
class Pipe(Filter):
    """Given a bunch of objects, Pipe puts them in a list and starts running them"""
    def __init__(self, *args):
        self.title = 'Pipe'
        self.filter_list = args
        
    def __eq__(self, other):
        return self.title == other.title
    
    def run(self):
        """RUN runs the filters Reader, Trim, Head, and Sort and 
        outputs the results to a list of lists. The outer list
        contains lists of the output from each record for all of the
        filters included when initializing Pipe.
        """
        self.record = []
        self.results = []
        streaming = True
        while streaming:
            filter_output = []
            for filter in self.filter_list:
                record = filter.next_record(self.record)
                filter_output.append(record)
                if filter == Reader():
                    self.record = record
                    if record == None:
                        streaming = False
                        
            self.results.append(filter_output)
        return self.results


        

                      
            
                
                
