# =========== condition ============= #

# relational operatores
# used to return a boolean value to condition
great_then = 10 > 1 # return true
less_then = 10 < 1 # return false
great_or_equal_then = 10 >= 1 # return true
less_or_equal_then = 10 <= 1 # return false
diferent = 10 != 1 # return true
equal = 10 == 1 # return false

# logical operatores
# used to join conditions
op_and = 10 > 1 and 10 < 60
op_or = 10 > 1 or 10 > 4
op_not = not(10 > 1)

a = 10
b = 11

if a > b:
    print("a is greater then b")
else:
    print("b is greater then a")

print('a is greater then b' if a < b else 'b is greater then a')
