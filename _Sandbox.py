# 0 1 1 2 3 5 8 13
#5
def nthFib(n):
    a = 0
    b = 1
    for num in range(1,n -1):
        temp = b
        b = a + b
        a = temp
    return b
    
print(nthFib(5))



def nthFib(n):
    FibArray =  [0,1]
    counter = 3
    while counter <= n:
        nextFib = FibArray[0] + FibArray[1]
        FibArray[0] = FibArray[1]
        FibArray[1] = nextFib
        counter +=1
    return FibArray[1] if n>1 else FibArray[0]



def nthFib(n):
    
    lastTwo = [0,1 ]
    counter = 3
    while counter <= n :
        nextFib = lastTwo[0] + lastTwo[1]
        lastTwo[0] = lastTwo[1]
        lastTwo[1] = nextFib
        counter += 1
        
    return lastTwo[1] if n > 1 else lastTwo[0]

