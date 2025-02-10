def factorial(N):
    result = 1
    for i in range(1, N + 1):
        result = result * i
    return result
N = int(input("Enter a number to calculate its factorial: "))
result = factorial(N)
print("The factorial of", N, "is", result)
