def factorial(x : int):
    value = 1
    for i in range(1, x + 1):
        value *= i
    return value
print(factorial(4))