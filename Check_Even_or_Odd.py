def oddOreven(n):
    if n%2==0:
        return "Even"
    else:
        return "Odd"

num = int(input("Enter a number : "))
print(f"{num} is an {oddOreven(num)} number.")