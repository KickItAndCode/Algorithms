from collections import Counter


def containsDuplicate(nums):
    map = {}
    for n in nums:
        if n in map:
            return True
        else:
            map[n] = True
    return False


def containsDuplicate2(nums):
    map = Counter(nums)
    for k, v in map.items():
        if v > 1:
            return True
    return False


print(containsDuplicate2([1, 2, 3, 4, 4]))  # true
print(containsDuplicate2([1, 2, 3, 4]))  # true
