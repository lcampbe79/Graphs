class MySet:
    def __init__(self):
        self.data = {}  # dictionary

    def add(self, d):
        # Ignore duplicates--sets only contain unique values

        # Everythis is O(1) in here

        if d not in self.data:
            self.data[d] = True  # add to set

    def delete(self, d):

        # Everythis is O(1) in here

        if d in self.data:
            del self.data[d]   # remove from set

    def is_in(self, d):
        # Test if in set

        # Everythis is O(1) in here

        return d in self.data

    def __str__(self):
        r = ''
        for d in self.data:
            if r != '':
                r += ','
            r += repr(d)

        return f'MySet<{r}>'

s = MySet()

s.add(1)
s.add(2)
s.add(3)
s.add(3)
s.add(3)
s.add(4)

print(s)
print(s.is_in(3))

s.delete(3)

print(s)
print(s.is_in(3))
