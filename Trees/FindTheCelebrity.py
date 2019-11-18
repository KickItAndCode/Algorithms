# 277  Find the Celebrity
# Description


# Suppose you are at a party with n people(labeled from 0 to n - 1) and among them, there may exist one celebrity. The definition of a celebrity is that all the other n - 1 people know him/her but he/she does not know any of them.

# Now you want to find out who the celebrity is or verify that there is not one. The only thing you are allowed to do is to ask questions like: "Hi, A. Do you know B?" to get information of whether A knows B. You need to find out the celebrity(or verify there is not one) by asking as few questions as possible(in the asymptotic sense).

# You are given a helper function bool knows(a, b) which tells you whether A knows B. Implement a function int findCelebrity(n), your function should minimize the number of calls to knows.

# There will be exactly one celebrity if he/she is in the party. Return the celebrity's label if there is a celebrity in the party. If there is no celebrity, return -1.

# if a knows be a can't be the celeb
# if b doesn't know a he could still be a celeb
def findCelebrity(n):
    candidate = 0
    for i in range(1, n):
        if knows(candidate, i):
            candidate = i
    for i in range(n):
        if i != candidate and knows(candidate, i) or not knows(i, candidate):
            return -1
    return candidate


print(findCelebrity(2))  # 1 Output: 1
# Explanation:
# Everyone knows 1,and 1 knows no one.

print(findCelebrity(3))  # 0 Output: Explanation:
# Everyone knows 0,and 0 knows no one.
# 0 does not know 1,and 1 knows 0.
# 2 knows everyone,but 1 does not know 2.
