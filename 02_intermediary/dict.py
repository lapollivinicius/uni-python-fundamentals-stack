# =========== dict ============= #

# it's similar to objects in js
# declare (key : value)
user = {
    'name': 'john',
    'age': 10
}

# to add a item use
user['genre'] = 'masc'

# to remove a item use
del user['genre']

# to get values
print(user.values())

# to get keys
print(user.keys())

# to get items
print(user.items())

# to iterate
for x, y in user.items():
    print(f'{x} is {y}')

# usually is used with list

users = [
    {'name' : 'john', 'age' : 10},
    {'name' : 'abby', 'age' : 13},
    {'name' : 'marie', 'age' : 24}
]

# to iterate use loops
for item in users:
    print(item['age'])