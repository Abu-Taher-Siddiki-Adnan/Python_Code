def Swap(a,b):
    a,b = b,a
    return a,b
x = int(input("X = "))
y = int(input("Y = "))
print(f"Before swapping X = {x} and Y = {y}")
p,q = Swap(x,y)
print(f"Before swapping X = {p} and Y = {q}")