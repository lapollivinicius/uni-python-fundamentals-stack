def factorial(n):
    f = 1
    for c in range(1, n+1):
        f *= c
    return f

number_factorial = factorial(2)

print(number_factorial)