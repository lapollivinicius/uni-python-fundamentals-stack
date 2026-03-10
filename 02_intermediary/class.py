# =========== class ============= #

# class define the shape of a object must be
# it's used to instantiate a object (part abstract)

# layers of class

# name - that will define
# attribute - attribute (shape) of object
# actions - methods that will change or manipulate the object

class PersonClass:

    '''
    this class create a person
    var = PersonClass(name, age)
    '''

    # attributes with constructor
    def __init__(self, name = '', age = ''):
        self.name = name
        self.age = age
        self.genre = ""
        self.email = ""

    # methods
    def changeName(self, n):
        self.name = n
    
    # methods default
    def __str__(self):
        return f'name is {self.name} and age is {self.age}'
    
# instantiate the object
user = PersonClass('john', 19)
user.email = 'john@email.com'

print(user.changeName('marie'))

print(user)
print(user.__doc__)

# can use DUNDER (__) to reveal some methods
# similar to prototypes in js

# will return the object
print(user.__getstate__()) 
print(user.__dict__) 

# to extends class use 
class Student(PersonClass):
  def __init__(self, name='', age=''):
      super().__init__(name, age)
  pass

# Polymorphism
# when you have multiple class with the same methods
# you can create a parent class and define children classes

class Vehicle:
    def __init__(self, brand="", year=""):
        self.brand = brand
        self.year = year
        pass

    def move(self):
        print(self.brand + ' move!')

class Car(Vehicle):
    pass

class Boat(Vehicle):
    pass

car1 = Car("FORD", "2000")
boat1 = Boat("MAVERICK", "1922")

boat1.move()

# Encapsulation
# Private - getters - setters methods
class AccountBank:
    def __init__(self, name):
        self.name = name
        self.__amount = 0
    
    def getAmount(self):
        return self.__amount
    
    def setAmount(self, amount):
        self.__amount = amount 

user = AccountBank('Mister John')
user.setAmount(1000)
print('your amount is US$', user.getAmount())

# we can declare a class inside class

class Outer:
    def __init__(self):
        self.name = 'Outer Class'
        pass

    class Inner:
        def __init__(self):
            self.name = "Inner Class"

outer = Outer()
inner = outer.Inner()
print(inner.name)
    