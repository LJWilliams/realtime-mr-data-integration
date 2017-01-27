 # -*- coding: utf-8 -*-
"""
Pipes and filters using Python classes.

e.g., 

    p = Pipe(Reader('mydata.txt'), Trim(20), Head(10), Sort())
    results = p.run()

will read 'mydata.txt', trim to 20 columns, take the first 10 lines, sort,
and print that as output.
Input is a txt file (strings) and returns a string delimited by |.
"""

class Filter():
    """Base class of all filters, intended for use in Pipe.
    """

    def __init__(self, title='Filter'):
        """Construct common elements of all filters."""
        self.title = title 
        self.upstream = None

    def finish(self):
        return None
    
    def finish_upstream(self): # needs to work on both NONE and upstream
        if self.upstream == None:
            self.finish()
    

    #def get_record(self, filters):

# FIXME: this is doing a search linear in the length of the pipeline
# for each record.  How about giving each Filter an 'upstream' member
# (set by Pipe when the Filters are constructed or when they're put
# into the pipeline)?

      #  index = [ filter.title for filter in filters ].index(self.title)
      #  if filters[index-1].title != self.title:
      #      status, record = filters[index-1].next_record(filters) # FIXME: see comment below
      #  return status, record
    

# FIXME: since every Filter child class is supposed to have a
# next_record method, I'd define something like this here:
#
# def next_record(self):
#   raise NotImplementedError('derived class must implement next_record')
#
# with a docstring explaining the return protocol (string plus record).


class Reader(Filter):
    """Produce lines of text from a file one by one.
    """

    def __init__(self, filename):
        super().__init__('Reader') # Good.
        self.file = open(filename)
        pass
      

    def finish(self):          
        self.file.close() # Good.
        self.upstream = None # ? will this work ????
        

    def next_record(self):
        if self.upstream == None:
            try:
                record = self.file.readlines(1)
            except:
                return None
        elif self.upstream != None:
           record = self.upstream.next_record()
        return record
                


class Trim(Filter):
    """Trim input records to 'ntrim' columns or less."""

    def __init__(self, ntrim=5):
        self.ntrim = ntrim
        self.trim = [] # FIXME: why accumulate? why not return one by one as records come in?
        super().__init__('Trim')  

    def next_record(self):
        if self.upstream == None:
            return None
        else:
            record = self.upstream.next_record()[0]
            return [record[:self.ntrim]]

class Head(Filter):
    """Echo the first N lines of input.
    """

    def __init__(self, nhead=5):
        super().__init__('Head')
        self.nhead = nhead
        self.index = 0
        
    def next_record(self):
        if self.upstream == None:
            record = None
        else:
            if self.index >= self.nhead:
                record = None
            else:
                record = self.upstream.next_record()
        self.index += 1
        return record

                
class Sort(Filter):
    """Sort all input records alphabetically.
    """

    def __init__(self):
        super().__init__('Sort')  
        self.sort = [] # FIXME: yes, this one needs to accumulate
     
    def finish(self):
        return sorted(self.sort)

    def next_record(self):
        if self.upstream == None:
            record = None
        else:
            record = self.upstream.next_record()
            if record != None:
                self.sort.append(record)
                return sorted(self.sort)

class Pipe():
    """Given a bunch of filters, run them in order.
    """

    def __init__(self, *args):
        self.filters = list(args)
        if len(self.filters) > 1:
            for filter in self.filters[1:]:
                index = self.filters.index(filter) - 1
                filter.upstream = self.filters[index]
        
    def run(self):
        """Run the given filters in order, passing the output of each to the next.
        """
        record = None
        while True:
            record = self.filters[-1].next_record()
            print(record)
            return record
            
                

# FIXME: if I follow the logic here correctly, this loops until the
# last filter says 'Closed', then returns a single record - unless the
# filters are always return records in lists?
