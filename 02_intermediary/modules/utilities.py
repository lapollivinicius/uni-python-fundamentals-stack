def factorial(n):
    f = 1
    for c in range(1, n+1):
        f *= c
    return f

def sum(*num):
    '''Use a list or tuple sum([])'''
    c = 0
    for n in num:
        c += n
    return c

def isEven(n):
    '''This return a boolean value'''
    if n % 2 == 0: 
        return True
    else:
        return False
    
def average(*num):
    '''This return average from values'''
    total = 0
    for n in num:
        total += n
    return total / len(num)