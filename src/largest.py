def getLargestOfTuple(tuple):
    l = tuple[0]
    for i in tuple:
        if(i > l):
            l = i
    return l

# print(getLargestOfTuple((105,165,454,589,985,106)))

def getLargestBetween2(a,b):
    if(a > b):
        return a
    return b

# print(getLargestBetween2(1,2))
# print(getLargestBetween2(2,1))

def getLargestBetween3(a,b,c):
    return getLargestOfTuple((a,b,c))
    # if(a > b and a > c):
    #     return a
    # if(b > a and b > c):
    #     return b
    # return c
       
# print(getLargestBetween3(1,2,3))
# print(getLargestBetween3(1,3,2))
# print(getLargestBetween3(3,1,2))

def getLargestBetween4(a,b,c,d):
    return getLargestOfTuple((a,b,c,d))
    # if(a > b and a > c and a > d):
    #     return a
    # if(b > a and b > c and b > d):  
    #     return b
    # if(c > a and c > b and c > d):
    #     return c
    # return d

# print(getLargestBetween4(1,2,3,4))
# print(getLargestBetween4(1,3,4,2))
# print(getLargestBetween4(3,4,1,2))
# print(getLargestBetween4(4,3,1,2))


def getLargestOfTupleOdd(tuple):
    if(len(tuple)==0):
        return None
    l = None
    if(tuple[0] % 2 == 1):
        l = tuple[0]
    for i in tuple:
        if(i % 2 == 1):
            if(l == None or i > l):
                l = i
    return l

# print(getLargestOfTupleOdd(()))
# print(getLargestOfTupleOdd((2,4,6,8,5,6)))
