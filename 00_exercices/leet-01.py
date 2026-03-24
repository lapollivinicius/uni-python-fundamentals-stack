
nums = [2, 14, 11, 12, 15]
target = 26

def twoSum(nums, target):
    seen = {}
    for i, value in enumerate(nums):
        complemento = target - value
        if complemento in seen:
            return [seen[complemento], i], seen
        seen[value] = i

print(twoSum(nums, target))  