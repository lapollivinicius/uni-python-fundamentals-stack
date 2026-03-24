# highest number

list = [2, 62, 1, 6, 10]

def highestNumber(num):
  n = num[0]
  for i in range(len(num)):
    if num[i] > n:
      n = num[i]
    
  return n

print(highestNumber(list))