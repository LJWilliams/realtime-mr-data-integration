 # -*- coding: utf-8 -*-
"""
Pipes and filters using Python classes.

e.g., 

    p = Pipe(Reader('mydata.txt'), Trim(20), Head(10), Sort())
    results = p.run()

will read 'mydata.txt', trim to 20 columns, take the first 10 lines, sort,
and print that as output.
Input is a txt file (strings) and returns a string.
"""


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
        self.file = open(filename)
      
    def finish(self):
        self.file.close()
        return self
        
    def next_record(self, status, record):
        status = 'Open'
        if not self.file.closed: 
            try:
                record = self.file.readlines(1)[0]
            except IndexError:
                self = Reader.finish(self)
                return 'Closed', str(record)
            return status, record
        else:
            if record == None:
                status = 'Closed'
                return status, record


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
            if record != None:
                return status, '\t'.join(self.trim)
            elif record == None:
                return status, None  

                
class Head(Filter):
    """Echo the first N lines of input.
    """

    def __init__(self, nhead=5):
        super().__init__('Head')
        self.nhead = nhead
        

    def next_record(self, status, record):
        if status == 'Open':
            if record == None:
                return status, None
            elif record != None:
                return status, record[:self.nhead]
        elif status == 'Closed':
            if record != None:
                return status, '\t'.join(record.split('\t')[:self.nhead])
            elif record == None:
                return status, None

                
class Sort(Filter):
    """Sort all input records alphabetically.
    """

    def __init__(self):
        super().__init__('Sort')        

    def next_record(self, status, record):
        if status == 'Open':
            if record == None:
                return status, None
            elif record != None:
                record = sorted(list(record))
                return status, record
        elif status == 'Closed':
            if record == None:
                return status, None
            elif record != None:
                return status, '\t'.join(sorted(record.split('\t')))       


class Pipe():
    """Given a bunch of filters, run them in order.
    """

    def __init__(self, *args):
        self.filters = args 
    

    def run(self):
        """Run the given filters in order, passing the output of each to the next.
        """

        record = None
        status = None
        while True:
            for filter in self.filters:
                status, record = filter.next_record(status, record)
            if status == 'Closed':
                return record # This only returns the last record if Head or Sort act on the output of Reader. Would it ever be necessary to return the output of each record as a push? I can see pulling through the pipeline if a structural scan is written to disk, but it would be good to have the option for data types I haven't considered yet. However, if I move the return statement to get the individual records, Pipe acts like an iterator, pausing to wait for the next call to Pipe.run(). Any suggestions? 
