def Sum(a,n):
    sum = 0
    for i in range(a,n+1):
        sum+=i
    return sum
a = int(input("Enter the starting value : "))
b = int(input("Enter the ending value : "))
print(f"The summation of the natural number from {a} to {b} is {Sum(a,b)}")