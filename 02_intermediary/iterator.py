# =========== iterator ============= #

# it's is an object to iterate values

# we can declare from tuple set or something else
mytuple = (1, 10, 100)

myinterator = iter(mytuple)

# to every next() myinterator recive other value being first next the first value
print(next(myinterator))
next(myinterator)
print(next(myinterator))

# to create iterator as an object or class use __iter__ instead __init__

class Numbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x
    
myclass = Numbers()
myiter = iter(myclass)