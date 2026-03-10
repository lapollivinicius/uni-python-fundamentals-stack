# =========== json ============= #

# to work with json in py we need to know some tools to convert

# use the module json
import json

# there two main methods that we can use

myjson = '{ "name":"John", "age":30, "city":"New York"}'

# to load/convert json to py
x = json.loads(myjson)

print(f'in py {x}')

# and to convert py to json we can use dumps()
y = json.dumps(x)

print(f'in json {y}')

# when we convert, this change types to js equivalent

# PYTHON	JAVASCRIPT
# dict	    Object
# list	    Array
# tuple	    Array
# str	    String
# int	    Number
# float	    Number
# True	    true
# False	    false
# None	    null

# we can pass others params 

# indent=4 - define the indentation
# separators=(". ", " = ") - define the separator 
# sort_keys=True - sort the keys orders

z = json.dumps(x, indent=4, separators=(". ", " = "), sort_keys=True)