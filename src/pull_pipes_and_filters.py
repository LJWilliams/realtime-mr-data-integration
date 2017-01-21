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

#import polling

class Filter():
    """Base class of all filters, intended for use in Pipe.
    """

    def __init__(self, title='Filter'):
        """Construct common elements of all filters."""
        self.title = title 

    def finish(self): 
        return None
    
    def get_record(self, filters):
        index = [ filter.title for filter in filters ].index(self.title)
        if filters[index-1].title != self.title:
            status, record = filters[index-1].next_record(filters)
        return status, record


class Reader(Filter):
    """Produce lines of text from a file one by one.
    """

    def __init__(self, filename):
        super().__init__('Reader')
        self.file = open(filename)
      
    def finish(self):
        self.file.close()
        return self
        
    def next_record(self, filters):
        if not self.file.closed:
            status = 'Open'
            try:
                record = self.file.readlines(1)[0]
            except IndexError:
                self = Reader.finish(self)
                return 'Closed', None
            return status, record  
        else:
            return 'Closed', None


class Trim(Filter):
    """Trim input records to 'ntrim' columns or less."""

    def __init__(self, ntrim=5):
        super().__init__('Trim')
        self.ntrim = ntrim
        self.trim = []
        self.filter2call = None
          
    def next_record(self, filters):
        status, record = super().get_record(filters)
             
        if status == 'Open':
            if record != None and record.count('\n') == 1:
                self.trim.append(record[:self.ntrim])
                return  'Open', None
            elif record != None and record.count('\n') > 1:
                return 'Closed', ' | '.join(item[:self.ntrim] for item in record.split(' | '))
            elif record == None:
                return 'Open', None
        elif status == 'Closed':
            if len(self.trim) == 0:
                return  status, ' | '.join(item[:self.ntrim] for item in record.split(' | '))
            else:
                return  status, ' | '.join(self.trim)


                
class Head(Filter):
    """Echo the first N lines of input.
    """

    def __init__(self, nhead=5):
        super().__init__('Head')
        self.nhead = nhead
        self.head = []
        self.index = 0
        
        
    def next_record(self, filters):
        status, record = super().get_record(filters)
        if status == 'Open':
            if record != None and record.count('\n') == 1:
                #if self.index <= self.nhead:
                self.head.append(record)
                self.index += 1
                return status, None
            elif record != None and record.count('\n') > 1:
                return 'Closed', ' | '.join(record.split(' | ')[:self.nhead])
            elif record == None:
                return status, None
        elif status == 'Closed':
            if len(self.head) == 0:
                return status, ' | '.join(record.split(' | ')[:self.nhead])
            else:
                return status, ' | '.join(self.head[:self.nhead])


                
class Sort(Filter):
    """Sort all input records alphabetically.
    """

    def __init__(self):
        super().__init__('Sort')  
        self.sort = []

    def next_record(self, filters):
        status, record = super().get_record(filters)
        if status == 'Open':
            if record != None and record.count('\n') == 1:
                self.sort.append(record)
                return status, None
            elif record != None and record.count('\n') > 1:
                return 'Closed', ' | '.join(sorted(record.split(' | ')))  
            if record == None:
                return status, None
        elif status == 'Closed':
            if len(self.sort) == 0:
                return status, ' | '.join(sorted(record.split(' | ')))       
            else:
                return status, ' | '.join(sorted(self.sort))

class Pipe():
    """Given a bunch of filters, run them in order.
    """

    def __init__(self, *args):
        self.filters = args 

    def run(self):
        """Run the given filters in order, passing the output of each to the next.
        """
        
        while True:
            status, record = self.filters[-1].next_record(self.filters)
            if status == 'Closed':
                return record

            
       
