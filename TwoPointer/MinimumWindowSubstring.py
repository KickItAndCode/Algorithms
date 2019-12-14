# 76. Minimum Window Substring

# Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

# Example:

# Input: S = "ADOBECODEBANC", T = "ABC"
# Output: "BANC"
# Note:

# If there is no such window in S that covers all characters in T, return the empty string "".
# If there is such window, you are guaranteed that there will always be only one unique minimum window in S.

# looking for the smallest window that satifies the same number of characters in t
# brute force way is looking at all the windows and compare them and take the smallest

# more efficient approach utilizes two pointers in a sliding window type of approaches

# Time O (S+T) space  O (S +T)
from collections import Counter


def minWindow(s, t):

    if not t or not s:
        return ""

    # Dictionary which keeps a count of all the unique characters in t.
    dict_t = Counter(t)

    # Number of unique characters in t, which need to be present in the desired window.
    required = len(dict_t)

    # left and right pointer
    l, r = 0, 0

    # formed is used to keep track of how many unique characters in t are present in the current window in its desired frequency.
    # e.g. if t is "AABC" then the window must have two A's, one B and one C. Thus formed would be = 3 when all these conditions are met.
    formed = 0

    # Dictionary which keeps a count of all the unique characters in the current window.
    window_counts = {}

    # ans tuple of the form (window length, left, right)
    ans = float("inf"), None, None

    while r < len(s):

        # Add one character from the right to the window
        character = s[r]
        window_counts[character] = window_counts.get(character, 0) + 1

        # If the frequency of the current character added equals to the desired count in t then increment the formed count by 1.
        if character in dict_t and window_counts[character] == dict_t[character]:
            formed += 1

        # Try and contract the window till the point where it ceases to be 'desirable'.
        while l <= r and formed == required:
            character = s[l]

            # Save the smallest window until now.
            if r - l + 1 < ans[0]:
                ans = (r - l + 1, l, r)

            # The character at the position pointed by the `left` pointer is no longer a part of the window.
            window_counts[character] -= 1
            if character in dict_t and window_counts[character] < dict_t[character]:
                formed -= 1

            # Move the left pointer ahead, this would help to look for a new window.
            l += 1

        # Keep expanding the window once we are done contracting.
        r += 1
    return "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]


def minWindow(s, t):
    need = Counter(t)  # hash table to store char frequency
    missing = len(t)  # total number of chars we care
    start, end = 0, 0
    i = 0
    for j, char in enumerate(s, 1):  # index j from 1
        if need[char] > 0:
            missing -= 1
        need[char] -= 1
        if missing == 0:  # match all chars
            while i < j and need[s[i]] < 0:  # remove chars to find the real start
                need[s[i]] += 1
                i += 1
            # make sure the first appearing char satisfies need[char]>0
            need[s[i]] += 1
            missing += 1  # we missed this first char, so add missing by 1
            if end == 0 or j-i < end-start:  # update window
                start, end = i, j
            i += 1  # update i to start+1 for next window
    return s[start:end]


# sliding window problem
# count all chars in string T
# left pointer point to string which has been processed
# right pointer point to string, which has not been processed
# 1.if all window from left to right contains all string T(counter values all less then or equal to 0)
#   calculate min window length, and keep answer
#   then move left pointer
# 2.else there are missing string in current answer
#   move right pointer
#   update counter
# repeat 1, 2 steps until right is equal to len(s), then break it
def minWindow(self, s, t):
    left, right = 0, 0
    # count T chars
    counter = collections.defaultdict(int)
    for a in t:
        counter[a] += 1

    minwindow = len(s) + 1
    answer = None

    while right <= len(s):
        # check all chars in T are in the current answer
        if all(map(lambda x: True if x <= 0 else False, counter.values())):
            if minwindow > right-left:
                minwindow = right-left
                answer = s[left:right]
            char = s[left]
            if char in counter:
                counter[char] += 1
            left += 1
        else:
            if right == len(s):
                break
            char = s[right]
            if char in counter:
                counter[char] -= 1
            right += 1

    return answer if answer else ''


print(minWindow("ADOBECODEBANC", "ABC"))  # BANC
