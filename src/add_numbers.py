# def add_numbers():
#     num1 = float(input('Enter number 1: '))
#     num2 = float(input('Enter number 2: '))
#     num3 = float(input('Enter number 3: '))
#     num4 = float(input('Enter number 4: '))
#     num5 = float(input('Enter number 5: '))
#     return num1+num2+num3+num4+num5

# sum = add_numbers()
# print(sum)

def add_numbers():
    numbers = []
    for i in range(5):
        inp = input(f'Enter number {i + 1}: ')
        num = float(inp)
        numbers.append(num)
    return sum(numbers)

total = add_numbers()
print(f"The sum of numbers is: {total}")

# def add_numbers():
#     numbers = []
#     for index in range(5):
#         numbers.append(float(input(f'Enter number {index + 1}: ')))
#     return sum(numbers)

# print(f"The sum of numbers is: {add_numbers()}")
