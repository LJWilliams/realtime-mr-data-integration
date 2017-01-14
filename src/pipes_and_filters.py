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
        
        # FIXME: doesn't belong in the base class.  Only the classes
        # that interact with files ought to have this.  (The clue is that
        # the constructor doesn't set `self.text`.)  It's OK for derived
        # classes to add more data members that parent classes don't have.
        # It's less common for derived classes to add methods that their
        # parents don't have - if you expect to do this, it's common to
        # raise `NotImplementedError` in the parent class method.
    
    def __eq__(self, other):
        # FIXME: when do you actually rely on this?
        return self.title == other.title

                
    
        
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
        for line in self.file:
            return line
        

class Trim(Filter):
    """For each line of input, Trim produces one line of output trimmed to given number of elements"""
    def __init__(self, ntrim=5):
        Filter.__init__(self)
        self.ntrim = ntrim
        self.title = 'Trim'
 
    def __eq__(self, other):
        return self.title == other.title
          
    def next_record(self, record):
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
        self.index += 1
        if self.index <= self.nhead:
            return record 
        else:
            record = None
            return record
                
                
    
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
            return None
        
    
class Pipe(Filter):
    """Given a bunch of objects, Pipe puts them in a list and starts running them"""
    def __init__(self, *args):
        self.title = 'Pipe'
        self.filter_list = args
        

    def __eq__(self, other):
        return self.title == other.title
        
    def __iter__(self):
        return self
    
    def run(self):
        """RUN runs the filters Reader, Trim, Head, and Sort and 
        outputs the results of the last input filter
        
        data:  the output of the last filter run (default is Sort)  
        """
        self.record = []
        record = []
        results = []
        streaming = True
        while streaming:
            for filter in self.filter_list:
                filter_output = []
                record = filter.next_record(self.record)
                print(record)
                if filter == Reader(): # Is there a nicer way of running these if statements? It seems a little clunky to me, but I can't seem to see what the problem with it is
                    if record == None:
                        streaming = False
                        sort = self.filter_list.index(Sort())
                        record = self.filter_list[sort].next_record(record)
                        results = filter_output.append(record)
                        print(*record, '\n')
                        return results
                        break
                    else:
                        self.record = record
                results =  filter_output.append(record)
                print(results)
        

                      
            
                
                
