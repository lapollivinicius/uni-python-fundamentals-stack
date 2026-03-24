# numbers duplicated

list1 = [1,2,3,4]
list2 = [4,6,6,1]
list3 = [1,3,2,1]

def hasDuplicated(list):
  seen = set()
  for value in list:
    if value in seen:
      return True
    seen.add(value)
  return False

print(hasDuplicated(list1))