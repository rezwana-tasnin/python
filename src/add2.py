def sumOfTupleOdd(t):
    sum = 0
    for i in t:
        if(i % 2 == 1):
            sum = sum + i
    return sum

mytuple = (3,6,7,9,10) 

result = sumOfTupleOdd(mytuple)
# print(result)


def sumOfTupleEven(t):
    sum = 0
    for i in t:
        if(i % 2 == 0):
            sum = sum + i
    return sum

mytuple = (3,6,7,8,10) 

result = sumOfTupleEven(mytuple)
# print(result)

def sumOfRange(s,e):
    sum = e
    for i in range(s,e):
        sum = sum + i
    return sum

def sumOfRangeOdd(s, e):
    sum = 0
    if(e % 2 == 1):
        sum = e
    for i in range(s,e):
        if(i % 2 == 1):
            sum = sum + i
    return sum

print(sumOfRangeOdd(1, 4))

def sumOfRangeEven(s, e):
    sum = 0
    if(e % 2 == 0):
        sum = e
    for i in range(s,e):
        if(i % 2 == 0):
          sum = sum + i
    return sum
print(sumOfRangeEven(1, 5))