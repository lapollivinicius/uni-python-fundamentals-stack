# =========== modules ============= #

# this is my module
from modules.utilities import isEven
import modules.utilities as util
# as name - it's alias to module

# use a function/method inside util
print(isEven(10))

print(util.factorial(5))

# use import [lib] to import the complete lib
import math

# use from [lib] import [method] to import especific things
from math import ceil

# random lib
import random

print(random.random()) # return a number between 0 and 1
print(random.randint(0 , 10)) # return a number between that is in (start, end)

# =========== creating a module ============= #

# you may separate a folder and create a file with name "__init__"
# python will idenify the next files as modules

