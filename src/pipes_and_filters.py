 # -*- coding: utf-8 -*-
"""
Pipes and filters using Python classes.

e.g., 

    p = Pipe(Reader('mydata.txt'), Trim(20), Head(10), Sort())
    results = p.run()

will read 'mydata.txt', trim to 20 columns, take the first 10 lines, sort,
and print that as output.
"""


class Filter():
    """Base class of all filters, intended for use in Pipe.
    """

    def __init__(self, title='Filter'):
        """Construct common elements of all filters."""

        self.title = title # Makes override by child classes cleaner.

      

class Reader(Filter):
    """Produce lines of text from a file one by one.
    """

    def __init__(self, filename):
        Filter.__init__(self, 'Reader') # FIXME: have a look at how new-style classes are initialized in Python 3
        self.file = open(filename) # FIXME: who closes the file and when?
        

    def __iter__(self): # FIXME: when do you use the Reader directly in a loop?
        return self
    

    def __eq__(self, other):
        # FIXME: why do you need equality testing on filters?
        # If it's to compare filters against Reader, that's a sign of leaky design.
        return self.title == other.title
          

    def next_record(self, record):
        for record in self.file: # FIXME: not clear what this is doing.
            return record

        

class Trim(Filter):
    """Trim input records to 'ntrim' columns or less."""

    def __init__(self, ntrim=5):
        Filter.__init__(self, 'Trim')
        self.ntrim = ntrim

 
    def __eq__(self, other): # remove?
        return self.title == other.title

          
    def next_record(self, record):
        if record == None:
            return None # FIXME: explicit return value (since the other return is explicit)
        return record[:self.ntrim] # FIXME: no need for intermediate variable

  
            
class Head(Filter):
    """Echo the first N lines of input.
    """

    def __init__(self, nhead=5):
        Filter.__init__(self, 'Head')
        self.nhead = nhead
        self.index = 0


    def __eq__(self, other): # FIXME: remove?
        return self.title == other.title


    def __iter__(self): # used where?
        return self
        

    def next_record(self, record):
        # How about:
        # if record == None:
        #    return None
        # elif index > self.nhead:
        #    return None
        # else:
        #    self.index += 1
        #    return record
        # or something similar?
        if self.index <= self.nhead and record != None:
            self.index +=1
            return record 
        else:
            return

                
    
class Sort(Filter):
    """Sort all input records alphabetically.
    """

    def __init__(self):
        Filter.__init__(self, 'Sort')
        self.sort = []


    def __eq__(self, other): # FIXME: for what?
        return self.title == other.title
        

    def next_record(self, record):
        if record == None:
            return self.sort # FIXME: but when does the actual sorting take place?
            # FIXME: also, this returns a list where the others return a single record
        else:
            self.sort.append(record)
            return # 'return None' (all explicit or none explicit)

        
    
class Pipe(Filter):
    """Given a bunch of filters, run them in order.
    """

    def __init__(self, *args):
        self.title = 'Pipe'
        self.filters = args # 'filters' instead of 'filter_list' in case you change your mind about implementation
        

    def __eq__(self, other): # FIXME: why?
        return self.title == other.title
    

    def run(self):
        """Run the given filters in order, passing the output of each to the next.
        """

        # FIXME: we'll discuss this one...

        self.record = []
        self.results = []
        streaming = True
        while streaming:
            filter_output = []
            for filter in self.filters:
                record = filter.next_record(self.record)
                filter_output.append(record)
                if filter == Reader(): # FIXME: no no no no no....
                    self.record = record
                    if record == None:
                        streaming = False
                        
            self.results.append(filter_output)
        return self.results
