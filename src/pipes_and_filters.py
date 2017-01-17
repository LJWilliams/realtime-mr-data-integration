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

    def finish(self): 
        print('Closing', self.title)
        return None
    # some of the child classes can on each of filter objects in turn
    # do nothing hook 
    
class Reader(Filter):
    """Produce lines of text from a file one by one.
    """

    def __init__(self, filename):
        #super 
        #Filter.__init__(self, 'Reader') # FIXME: have a look at how new-style classes are initialized in Python 3 super function
        super().__init__('Reader')
        self.file = open(filename)
      
    def finish(self):
        status = 'Closed'
        record = None
        self.file.close()
        print('Closing', self.title, '...')
        return status, record, self.file
        
    # Reader behaves as sort does nothing until receives end of input   signal
    def next_record(self, status, record):
        status = 'Open'
        if not self.file.closed: 
            try:
                record = self.file.readlines(1)[0]
            except IndexError:
                return 'Closed', None
            return status, record
        else:
            if record == None:
                status = 'Closed'
                return status, record

    # close file override 
    # create method that does finish that  overrides finish in Filter

class Trim(Filter):
    """Trim input records to 'ntrim' columns or less."""

    def __init__(self, ntrim=5):
        super().__init__('Trim')
        self.ntrim = ntrim
        self.trim = []
          
    def next_record(self, status, record):
        if status == 'Open':
            if record != None:
                self.trim.append(record[:self.ntrim])
                return status, None
            elif record == None:
                return status, record
        elif status == 'Closed':
            if record == None:
                return status, '\n'.join(self.trim)
            elif record != None:
                return status, None
                
           # return 'Closed', None

  
            
class Head(Filter):
    """Echo the first N lines of input.
    """

    def __init__(self, nhead=5):
        super().__init__('Head')
        self.nhead = nhead
        self.head = []
        self.index = 0
        

    def next_record(self, status, record):
        if status == 'Closed' and record !=None:
                return status, record.split('\n')[:self.nhead]
       

           

# Behaviour of next_record method to reflect passing things off to next filter
                
    
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

        
    
class Pipe():
    """Given a bunch of filters, run them in order.
    """

    def __init__(self, *args):
        self.filters = args # 'filters' instead of 'filter_list' in case you change your mind about implementation
        

#    def __eq__(self, other): # FIXME: why?
#        return self.title == other.title
    

    def run(self):
        """Run the given filters in order, passing the output of each to the next.
        """

        # FIXME: we'll discuss this one...

        record = None
        status = None
        streaming = True
        while streaming:
            for filter in self.filters:
                status, record = filter.next_record(status, record)
                print(filter.title, status, record)
            if status == 'Closed' and record == None:
                streaming = False
        return record

        # output return_record needs to return pair, status and string magid values?
        # reengineer return_record
        # get end of data signal
        # cases Trim produces string