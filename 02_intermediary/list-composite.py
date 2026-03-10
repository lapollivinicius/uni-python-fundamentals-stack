# =========== composite lists (matrix) ============= #

# lists 2D - X and Y direction
list = [[1,2,3],[4,5,6],[7,8,9]]

# index first and second list
list[1][1]

# use loop nested to iterate loop
for x in list:
    for y in x:
        print(y, end=' ')
    print('\n', end='')


