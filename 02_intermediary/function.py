# =========== function ============= #

# it's methods, actions, functions that can revice a parameter to apply a logic 

# start with a simple way
# this function return nothing, just apply logic

# first declare your function and logic
def sayHello():
    print('hello, world!')

# after call your function/method
sayHello() 

# now you can add parameters in ()
# it's a value that will used in logic inside function

# declare with ('variables kind')
# we can declare with default value to parameters (a=0, b=0)

# we can get var global using global var inside function
c = 10
def sum(a=0,b=0):
    global c
    print((a + b) * c)

# call with real values
sum(10,11)

# spread operator (...) -> (*args)
# when we can pass a (key=value) use (**args)
def sumList(*numbers):

    # to add docs use """ docs """
    """
    sum list of numbers \n
    sumList(list)
    """

    result = 0
    for num in numbers:
        result += num
    print(result)

sumList(1, 2, 3, 4, 5)

# function aside are called void function
# that don't return nothing
# but we can declare a function that will return something

def isEven(number):
    """ just put a number () and will return true or false """
    if number % 2 == 0:
        return True
    else:
        return False

print(isEven(11))

# generators and yield
# used to pause or to return a value from function

# use keyword yield to return and pause 
# it pause and when function was called again function will return you process from yield that was paused

def gen():
  yield 1
  yield 2
  yield 3

for value in gen():
  print(value)

# lambda is small way and annonymous that define a funcion
# var = lambda parameters : expression that will returned

x = lambda a : a + 10
print(x(5))

# decorators
# they are a way to pass a function as parameter to another function

# define the MainFunction
def changeUpper(sayHi):
    def inner(name):
        return sayHi(name).upper()
    return inner

# use @MainFunction and below the function that will be the parameter
@changeUpper
def sayHi(name):
    return f'hi, {name}'

# output
print(sayHi('john'))