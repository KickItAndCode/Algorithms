# def getNthFib(n):
#   a = 0
#   b = 1
#   c = 0

#   if n == 0: return a
#   if n == 1: return b
#   for i in range(2, n +1):
#     c = a + b
#     a = b
#     b = c
#     print(b)
  
#   return c
def getNthFib2(n):
  if n < 0:
    print("Incorrect Input")
  elif n == 0:
    return 0
  elif  n == 1:
    return 1
  else:
   return getNthFib(n -2) + getNthFib(n -1)

#O(N) Time | O(1) space
def getNthFib2(n):
  lastTwo = [0,1]
  counter = 3
  while counter <= n:
    nextFib = lastTwo[0] + lastTwo[1]
    lastTwo[0] = lastTwo[1]
    lastTwo[1] = nextFib
    counter += 1
  return lastTwo[1] if n>1 else lastTwo[0]


# technical using dynamic programming or memoization
def getNthFib(n):
  FibArray = [0, 1]

  # Get all to 0 up to n for later comparisons
  while len(FibArray) < n + 1:  
    FibArray.append(0)  

  if n <= 1:
    return n

  # calculate fib for elements prior to it
  else:
    if FibArray[n-1] == 0:
      FibArray[n-1] = getNthFib(n-1)

    if FibArray[n-2] == 0:
      FibArray[n -2] = getNthFib(n-2)

  FibArray[n] = FibArray[n-2] + FibArray[n-1]
  return FibArray[n]

#better memo
def getNthFib(n, memo= {1:0, 2:1}):
  if n in memo:
    return memo[n]
  else:
    memo[n] = getNthFib(n-1, memo) + getNthFib(n-2, memo)
    return memo[n]


print(f"Answer is : {getNthFib(9)}")
