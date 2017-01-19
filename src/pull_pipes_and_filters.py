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

import time

class Filter():
    """Base class of all filters, intended for use in Pipe.
    """

    def __init__(self, title='Filter'):
        """Construct common elements of all filters."""
        self.title = title 

    def finish(self): 
        return None
     
    
class Reader(Filter):
    """Produce lines of text from a file one by one.
    """

    def __init__(self, filename):
        super().__init__('Reader')
        self.filename = filename
      
    def finish(self):
        self.file.close()
        return self
        
    def next_record(self, stream, record):
        if stream == 'Open':
            # if closed or doesn't exist, open self.filename
            try:
                if self.file.closed: 
                    self.file = open(self.filename)
            except AttributeError:
                self.file = open(self.filename)
            # get the record, or if there is none, return None
            try:
                record = self.file.readlines(1)[0]
            except IndexError:
                return stream, None
            return stream, record  
        elif stream == 'Closed':
            if record != None:
                self = Reader.finish(self)
                return stream, record
            elif record == None:
                return stream, None

class Trim(Filter):
    """Trim input records to 'ntrim' columns or less."""

    def __init__(self, ntrim=5):
        super().__init__('Trim')
        self.ntrim = ntrim
        self.trim = []
          
    def next_record(self, stream, record):
        if stream == 'Open':
            if record != None:
                self.trim.append(record[:self.ntrim])
                return stream, None
            elif record == None:
                return stream, None
        elif stream == 'Closed':
            if len(self.trim) == 0:
                return stream, ' | '.join(item[:self.ntrim] for item in record.split(' | '))
            else:
                return stream, ' | '.join(self.trim)  

                
class Head(Filter):
    """Echo the first N lines of input.
    """

    def __init__(self, nhead=5):
        super().__init__('Head')
        self.nhead = nhead
        self.head = []
        self.index = 0
        
        
    def next_record(self, stream, record):
        if stream == 'Open':
            if record == None:
                return stream, None
            elif record != None:
                if self.index <= self.nhead:
                    self.head.append(record)
                self.index += 1
                return stream, None
        elif stream == 'Closed':
            if len(self.head) == 0:
                return stream, ' | '.join(record.split(' | ')[:self.nhead])
            else:
                return stream, ' | '.join(self.head[:self.nhead])


                
class Sort(Filter):
    """Sort all input records alphabetically.
    """

    def __init__(self):
        super().__init__('Sort')  
        self.sort = []

    def next_record(self, stream, record):
        print(stream, record)
        if stream == 'Open':
            if record == None:
                return stream, None
            elif record != None:
                self.sort.append(record)
                return stream, None
        elif stream == 'Closed':
            if len(self.sort) == 0:
                return stream, ' | '.join(sorted(record.split(' | ')))       
            else:
                return stream, ' | '.join(sorted(self.sort))

class Pipe():
    """Given a bunch of filters, run them in order.
    """

    def __init__(self, *args):
        self.filters = args 
        
 

    def run(self):
        """Run the given filters in order, passing the output of each to the next.
        """

        record = None
        stream = 'Open' # Needs to send command to Filter to open file
        print('Use Ctrl-C to exit') # How to shut down loop
        while True:
            try:
                for filter in self.filters:
                    stream, record = filter.next_record(stream, record)
                    time.sleep(.1)
                    #print(filter.title, stream, record)
                if stream == 'Closed':
                    return record
            except KeyboardInterrupt:
                stream = 'Closed'
                pass
            
                

                
        
            #raise stored_exception[0], stored_exception[1], stored_exception[2]
        

