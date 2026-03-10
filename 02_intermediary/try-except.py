# =========== try Except ============= #

# we have four blocks 

# try - the function that will tested
# except - the way you will handle the error
# else - the logic that will be run if there's no error
# finally - the logic that will be run regardless of result of the try

# see the example

# try will run print(x) but it's is an error, so it will run except logic
try:
    print(x)
except NameError:
  print("Variable x is not defined")

# in case there're more errors
except:
    print("something else went wrong")

# else will only be run if there're no error
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

# finally will be run regardless to try
try:
  print(z)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

# RAISE similar to throw of js
# it's a way to throw and handle with errors
x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")