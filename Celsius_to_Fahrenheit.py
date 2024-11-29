def Fahrenheit(c):
    f = (c*9/5)+32
    return f
C = float(input("Enter the temperature in Celsius : "))
print(f"The temperature in Fahrenheit is : {Fahrenheit(C)}")