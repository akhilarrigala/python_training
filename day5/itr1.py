class StopError(Exception):
    def __init__(self):
        self. message = 'Number of iterations exceeded'
    
    def get_message(self):
        return self.message

class FibonacciIterator:
    def __init__(self, stop=10):
        self.stop = stop
        self.start = 0
        self.cur = 0
        self.next = 1

    def __iter__(self):
        return self

    def __next__(self):
        try:
            self.start += 1
            term = self.cur
            self.cur, self.next = self.next, (self.cur + self.next)
            if self.start >= self.stop:
                raise StopError
            return term
        except StopError as e:
            print(e.get_message())
            return
                
for term in FibonacciIterator(5):
    print(term, end = ' ')
    
print()

fi = FibonacciIterator(3)
print(fi.__next__())
print(fi.__next__())
print(fi.__next__())
print(fi.__next__())