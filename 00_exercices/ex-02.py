# how much is high then 5

list = [2, 5, 8, 10, 10]

def highestThenFive(list):
  count = 0
  for value in list:
    if value > 5:
      count += 1
  return count

print(highestThenFive(list))