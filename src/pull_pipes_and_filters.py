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
        self.status = 'Open'
        self.record = None

    def finish(self, filter):  
        print('Closing ' + filter.title)
        filter.status = 'Closed'
        return filter.record
    
    @staticmethod
    def finish_upstream(filter): 
        if filter.status != 'Closed':
            if filter.upstream == None:
                filter.finish(filter)
            elif filter.upstream != None:
                if filter.upstream.status == 'Open':
                    filter.finish_upstream(filter.upstream)
                elif filter.upstream.status == 'Closed':
                    filter.record = filter.finish(filter)  
            return filter.record
        

class Reader(Filter):
    """Produce lines of text from a file one by one.
    """

    def __init__(self, filename):
        super().__init__('Reader') # Good.
        self.file = open(filename)
        pass
      

    def finish(self, filter):  
        print('Closing ' + self.title)
        self.file.close() # Good.
        self.status = 'Closed'
        return self.record
        

    def next_record(self):
        if self.upstream == None:
            try:
                self.record = self.file.readlines(1)
            except:
                return None
        elif self.upstream != None:
           self.record = self.upstream.next_self.record()
        return self.record
                


class Trim(Filter):
    """Trim input self.records to 'ntrim' columns or less."""

    def __init__(self, ntrim=5):
        self.ntrim = ntrim
        super().__init__('Trim')  

    def next_record(self):
        if self.upstream == None:
            return None
        else:
            self.record = self.upstream.next_record()
            if self.record != None: 
                if len(self.record) > 0:
                    if type(self.record[0]) == str:
                        self.record = self.record[0][:self.ntrim]
                    elif type(self.record[0]) == list:
                        for index, subrecord in enumerate(self.record):
                            self.record[index] = [subrecord[0][:self.ntrim]]
                        return [self.record]


class Head(Filter):
    """Echo the first N lines of input.
    """

    def __init__(self, nhead=5):
        super().__init__('Head')
        self.nhead = nhead
        self.index = 0
        
    def next_record(self):
        if self.upstream == None:
            self.record = None
        else:
            self.record = self.upstream.next_record()
            if self.record != None:
                if self.record != list():
                    if type(self.record[0]) == str:
                        if self.index >= self.nhead:
                            self.record = None
                        elif type(self.record[0]) == list:
                            return self.record[:self.nhead]
        self.index += 1
        return self.record

                
class Sort(Filter):
    """Sort all input self.records alphabetically.
    """

    def __init__(self):
        super().__init__('Sort')  
        self.sort = [] 
     
    def finish(self, filter):
        print('Closing ' + self.title)
        self.status = 'Closed'
        return sorted(self.sort)

    def next_record(self):
        if self.upstream != None:
            self.record = self.upstream.next_record()
            if len(self.record) > 0:
                if self.record[0] != list():
                    if self.record != None:  
                        self.sort.append(self.record)
                        return sorted(self.sort)
                    elif self.record[0] == list:
                        return sorted(self.record)
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
        
        for filtertitle in ('Reader', 'Trim', 'Head', 'Sort'):
            self.rename_filters(filtertitle)
        
    def rename_filters(self, filtertitle):
        indices = [i for i, x in enumerate(self.filters) if x.title == filtertitle]
        for enum, index in enumerate(indices):
            self.filters[index].title = filtertitle + str(enum)
        
    def run(self):
        """Run the given filters in order, passing the output of each to the next.
        """
        record = None
        index = 0
        try:
            while True:
                record = self.filters[-1].next_record()
        except KeyboardInterrupt:
            while index < len(self.filters):
                record = self.filters[-1].finish_upstream(self.filters[-1])
                index += 1
            return record
                
