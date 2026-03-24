# two sum o(n2) solution

list = [2, 3, 4, 6, 9]
target = 15

def twoSum(list, target):
  seen = {}
  for i, value in enumerate(list):
    aux = target - value
    if aux in seen:
      return [seen[aux], i]
    seen[value] = i
    
print(twoSum(list, target))