def factorial_count(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
n = 5
factorial = factorial_count(n)
print(f"The factorial of {n} is {factorial}")