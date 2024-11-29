def Largest(x,y,z):
    if x>y and x>z:
        print(f"Largest number is {x}")
    elif y>x and y>z:
        print(f"Largest number is {y}")
    elif z>x and z>y:
        print(f"Largest number is {z}")
    else:
        print("Numbers are all equal")
a = int(input("A = "))
b = int(input("B = "))
c = int(input("C = "))
Largest(a,b,c)