# =========== sets ============= #

# we can build a set using {}
# different to dict, set will recive only values

myset = {'apple', 'banana', 'cherry'}

# they are unordered, unchangeable*, and unindexed.

print(myset[0]) # error 'cause set can be indexed

# instead change to list
print(list(myset)[0])

# we can build a set using constructor passing a tuple
mysecondset = set(('apple', 'banana', 'cherry'))



