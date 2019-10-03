# [1,2,5,2,6,7,4] = 5
# [1,3,4,3] = 3
# [a. b, c, a, a,b,c,b,b] = 3 

# Given a string, find the length of the longest substring without repeating characters.

# Example 1:

# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 

# 3. Longest Substring Without Repeating Characters

# def lengthOfLongestSubstring(self, s: str) -> int:
#   l = 0
#   r = 0
#   valD = {}
#   res = 0
#   for i in range(len(nums)):
#     curr = 0
#     if nums[i] in valD:
#       l += nums[i] + 1
#     else:
#       valD[nums[i]]= i
#       r += 1
#       curr += 1
#       res = max(res +1 ,curr )
#     print(res)
#     return res


# working
def lengthOfLongestSubstring(s):
    dic, res, start, = {}, 0, 0
    for i, ch in enumerate(s):
        # when char already in dictionary
        if ch in dic:
            # check length from start of string to index
            res = max(res, i-start)
            # update start of string index to the next index
            start = max(start, dic[ch]+1)
        # add/update char to/of dictionary 
        dic[ch] = i
    # answer is either in the begining/middle OR some mid to the end of string
    return max(res, len(s)-start)


print(lengthOfLongestSubstring("abcabcbb"))

