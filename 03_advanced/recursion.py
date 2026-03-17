list = [2,4,6]

def sum(n):
    if n == []:
        return 0
    return n[0] + sum(n[1:])

print(sum(list)) 