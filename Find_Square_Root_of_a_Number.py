def sqrt__root(n):
    root = n**0.5
    newnum = int(root)
    if root-newnum>0:
        return False
    else:
        return True

num = int(input("Enter a number : "))
if sqrt__root(num):
    print(f"{num} is a perfect square number")
    print(f"Square root of {num} is : {int(num**0.5)}")
else:
    print(f"{num} is not a perfect square nunmber")