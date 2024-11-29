def Reverse(n):
    rev = 0
    while n != 0:
        rem = n % 10
        rev = rev * 10 + rem
        n = n // 10 
    return rev

user_input = int(input("Enter a number : "))
print(Reverse(user_input))