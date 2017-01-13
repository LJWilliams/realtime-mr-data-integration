 # -*- coding: utf-8 -*-
"""
Pipes, Filters & Classes

e.g., 
    p = Pipe(Reader('mydata.txt'), Trim(20), Head(10), Sort())
    results = p.run()
"""


import time


class Filter():
    """Base class that knows how to read and write data streams.
    Likely to end up as a queue of some sort.
    """

    def __init__(self):
        """Construct common elements of all filters."""

        self.datagen = [] # FIXME: what is this for?
        self.data = [] # FIXME: what is this for, and does every filter need it?
        self.streaming = True # FIXME: what does this do?
        self.record = [] # FIXME: what does this do, and why is it initialized to a list?
        self.index = [] # FIXME: what is this, and why is it initialized to a list?
        self.file = [] # FIXME: do all filters have a file?
        self.title = 'Filter' # This one, I can guess... :-)
        
        
    def __iter__(self):
        # FIXME: doesn't belong in the base class.  Only the classes
        # that interact with files ought to have this.  (The clue is that
        # the constructor doesn't set `self.text`.)  It's OK for derived
        # classes to add more data members that parent classes don't have.
        # It's less common for derived classes to add methods that their
        # parents don't have - if you expect to do this, it's common to
        # raise `NotImplementedError` in the parent class method.
        with open(self.text) as self.file:
            for line in self.file:
                time.sleep(.25)
                yield line

                
    def __eq__(self, other):
        # FIXME: when do you actually rely on this?
        return self.title == other.title

                
    def stop_stream(self, streaming=False):
        # Why does `Filter` have a list of other filters?  That belongs in
        # `Pipe`.  Also, any time a parent class refers to a specific child
        # class (as you're doing here with the comparison with `Sort`) it's
        # a sign that something has gone wrong in the class design.  Again,
        # you could have a `stop_stream` here that raises `NotImplementedError`,
        # and then override it in child classes that actually do something
        # interesting.
        for filter in self.filter_list:
            if filter != Sort():
                data = 'Only data from Sort() saved to output'
            else:
                data = self.retrieve_data(filter, streaming)
        return self, data

        
    def retrieve_data(self, filter, streaming):
        # See comment on `stop_stream` above.
        if filter == Sort():
            data = filter.next_record(streaming)
            data = list(data)
            data.pop(0)
            # save to sql database
            return self, data
        else:
            return
        
      # To come soon!

      
class Reader(Filter):
    """Class that produces output of Filter. Returns single record.
    """

    def __init__(self, text='haiku.txt'):
        Filter.__init__(self)
        self.record = [] # FIXME: redundant - this is done in the parent class.
        self.text = text # FIXME: only needs to be done here - parent class shouldn't have
                         # a `self.text` at all.
        self.title = 'Reader' # Good - override the default setting in the parent.

        
    def __eq__(self, other):
        return self.title == other.title

        
    def next_record(self, *args):
        self.streaming = args[0]
        if self.streaming == False: # FIXME: "if not self.streaming"
            return self, self.record # FIXME: why return self?  In fact, why return anything?
                                     # Looking at `Pipe.run`, the return value of `next_record`
                                     # is never used...?
        else:
            self.record = args[1]    # FIXME: so sometimes this produces two values,
                                     # and sometimes it produces `None` because of fall-through?
            #print(self.record)
  
            
class Trim(Filter):
    """For each line of input, Trim produces one line of output trimmed to given number of elements"""
    def __init__(self, ntrim=5):
        Filter.__init__(self)
        self.ntrim = ntrim
        self.trim = []
        self.title = 'Trim'

        
    def __eq__(self, other):
        return self.title == other.title
        
        
    def next_record(self, *args):
        self.streaming = args[0]
        if self.streaming == False:
            return self, self.trim
        else:
            record = args[1]
            self.trim = record[:self.ntrim]
           # print(self.title)
            print(self.trim)  

  
            
class Head(Filter):
    """Echos the first n lines (default = 5) of input unchanged, then stops producing output"""
    def __init__(self, nhead=5):
        Filter.__init__(self)
        self.nhead = nhead
        self.head = []
        self.title = 'Head'

    def __eq__(self, other):
        return self.title == other.title
        
    def next_record(self, *args):
        self.streaming = args[0]
        if self.streaming == False:
            return self, self.head
        else:
            record = args[1]
            index = args[2]
            type(index)
            if index < self.nhead:
                self.head.append(record)
                #print(self.title)
                print(record)    

                
                
    
class Sort(Filter):
    """Waits until it has read all of the input, then starts producing output"""
    def __init__(self):
        Filter.__init__(self)
        self.sort = []
        self.title = 'Sort'

    def __eq__(self, other):
        return self.title == other.title
        
    def next_record(self, *args):
        streaming = args[0]
        if streaming == False:
            #print(self.title)
            print(*self.sort,sep='\n')
            return self, self.sort
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
        self.title = 'Pipe'

    def __eq__(self, other):
        return self.title == other.title
        
    
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
        else:
            self.stop_stream(streaming)
        return self
