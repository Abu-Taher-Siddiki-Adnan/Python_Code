def factorial(x):
    fact = 1
    for i in range(1,x+1):
        fact*=i
    return  fact

n = int(input("Enter a positive number : "))
ans = factorial(n)
print(f"Factorial of {n} = {ans}")