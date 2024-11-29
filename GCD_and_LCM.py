def GCD(a,b):
    num1 = a
    num2 = b
    while num2 != 0:
        rem = num1 % num2
        num1 = num2
        num2 = rem
    return num1

def LCM(a,b):
    return (a * b) // GCD(a,b)

a = int(input("Enter a number : "))
b = int(input("Enter another number : "))
print(f"GCD of {a} and {b} is : {GCD(a,b)}")
print(f"LCM of {a} and {b} is : {LCM(a,b)}")