
def add(a,b):
        return a + b

def add3Numbers(a,b,c):
        return a + b + c

def summationOfNumbers(n):
        i = 1
        sum = 0
        while(i <= n):
               sum += i
               i += 1
        return sum 

def summationOfNumbersUsingRange(n):
        sum = 0
        for i in range(n):
               sum += (i + 1)             
        return sum

def summationOfRange(startingNumber, endingNumber):
        i = startingNumber
        sum = 0
        while(i <= endingNumber):
               sum += i
               i += 1
        return sum 

def summationOfRange2(startingNumber, endingNumber):
        sum = endingNumber
        for i in range(startingNumber, endingNumber):
               sum += i     
        return sum

def summationOfTuple(t):
        sum = 0
        for i in t:
              sum += i
        return sum

def summationOfTupleOfOdd(t):
        sum = 0
        for i in t:
             if(i % 2 == 1):
                     sum += i
        return sum

def summationOfTupleOfEvent(t):
        sum = 0
        for i in t:
             if(i % 2 == 0):
                     sum += i
        return sum

# print(add(100, 200))
# print(add3Numbers(56, 48, 65))

# print(summationOfNumbers(100))
# print(summationOfNumbersUsingRange(100))
# print(summationOfRange(1, 5))
# print(summationOfRange2(1, 5))

# print(summationOfTuple((65, 87, 78)))
# print(summationOfTuple((1, 2, 3)))

print(summationOfTupleOfOdd((1,2,3,4,5)))
print(summationOfTupleOfEvent((1,2,3,4,5)))    