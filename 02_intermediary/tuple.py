# =========== tuple ============= #

# it's similar to set in js 
fruits = ('banana', 'apple', 'pineapple')

# to get by index
print(fruits[0])

# can be iterated using loops
for a in fruits:
    print(a)

# we can know your size
print(len(fruits))

# tuple are not mutable after creation

# -------------- methods -------------- #

# use value to get index
fruits.index('apple') # return 0

# to sort the 'list' (don't change tuple)
fruits.sorted() # return names A -> Z 

# to count how many some item have
fruits.count('apple') # return 1



