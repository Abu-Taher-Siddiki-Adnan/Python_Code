def is_Palindrome(x):
    x = x.replace(" ","").lower()
    return x == x[::-1]
s = input("Enter a String or a number to check Palindrome : ")
if is_Palindrome(s):
    print(f"{s} is Palindrome")
else:
    print(f"{s} is not Palindrome")