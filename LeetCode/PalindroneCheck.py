# Write a function that takes in a non-empty string and that returns a
#  boolean representing whether or not the string is a palindrome. A 
#  palindrome is defined as a string that is written the same forward 
# #  and backward.
# Sample input: "abcdcba"
# Sample output: True (it is a palindrome)
def isPalindrome(string):

  i = 0
  j = len(string) -1
  res = True
  while i <= j :
    if string[i] != string[j]:
      res = False

    i +=1
    j -=1
  return res

print(isPalindrome("abcdcba"))
print(isPalindrome("abcdcb"))