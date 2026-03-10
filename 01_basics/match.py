# =========== match (switch) case ============= #

a = 13

match a:
    case 1:
        print('1')
    case 2:
        print('2')
    case _:
        print('default')

# (_) underscore acts as default

# in match different to switch we can combine values

month = 5
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")