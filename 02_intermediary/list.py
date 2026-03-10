# =========== list (array) ============= #

# it's similar to arrays in js 
fruits = ['pineapple', 'berry', 'apple']

# declare using list()

numbers = list()
numbers.append(134)
numbers.append(3234)

print(numbers)

# -------------- methods -------------- #

# to add item (push)
fruits.append('orange')

# to add item in index (index, value)
fruits.insert(0, 'limon')

# to remove a item (pop)
fruits.remove('apple')

# to remove a item (index)
fruits.pop(2)
del fruits[0]

# with condition 
if 'pineapple' in fruits:
    fruits.remove('pineapple')

fruits.append('pitaya')
fruits.append('blueberry')

# to sort item inside list (reverse=True = Z -> A)
fruits.sort(reverse=True)

# to get how many items have
howmany = len(fruits)

print(fruits, howmany)



