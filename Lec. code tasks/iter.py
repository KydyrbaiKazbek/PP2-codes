class EvenIterator:
    def __init__(self, N):
        self.n = N

    def __iter__(self):
        self.num = 2
        return self
    
    def __next__(self):
        if self.num<self.n:
            s = self.num
            self.num+=2
            return s
        else:
            raise StopIteration

x = EvenIterator(13)
for i in x:
    print(i)

print(next(x))