# 881. Boats to Save People
# The i-th person has weight people[i], and each boat can carry a maximum weight of limit.

# Each boat carries at most 2 people at the same time, provided the sum of the weight of those people is at most limit.

# Return the minimum number of boats to carry every given person.  (It is guaranteed each person can be carried by a boat.)


# Example 1:

# Input: people = [1,2], limit = 3
# Output: 1
# Explanation: 1 boat (1, 2)
# Example 2:

# Input: people = [3,2,2,1], limit = 3
# Output: 3
# Explanation: 3 boats (1, 2), (2) and (3)
# Example 3:

# Input: people = [3,5,3,4], limit = 5
# Output: 4
# Explanation: 4 boats (3), (3), (4), (5)
# Note:

# 1 <= people.length <= 50000
# 1 <= people[i] <= limit <= 30000


# 1 2 2 3  Limit 3

# 3  boat
# 2  Limit - i = 1

# Sort the array
# try and save the heaviest and the lightest each time
# if you cant save both save the heaviest
# using a sliding window at the front and back

def numRescueBoats(people, limit):
    res = 0
    people.sort()
    i, j = 0, len(people) - 1
    while i <= j:
        res += 1
        if people[i] + people[j] <= limit:
            i += 1
        j -= 1
    return res


print(numRescueBoats([3, 2, 2, 1], 3))  # 3
print(numRescueBoats([2, 2], 6))  # 1
