
def inputList(n):
    numbers = []
    for i in range(n):
        inp = input(f'Enter number {i + 1}: ')
        num = float(inp)
        numbers.append(num)
    return numbers

def sumOfList(list):
    return sum(list)

def getN():
    n = input(f'How many numbers to sum?')
    return int(n)

n = getN()
list = inputList(n)
total = sumOfList(list)

print(f"The sum of {n} numbers is: {total}")