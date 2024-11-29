import math
def find_area(x,y,z):
    if x**2 == y**2 + z**2:
        return (0.5 * y * z)
    else:
        s = (x+y+z) * 0.5
        return math.sqrt(s*(s-a)*(s-b)*(s-c))

a = int(input("Enter the largest side of the triangle : "))
b = int(input("Enter the second large side of the triangle : "))
c = int(input("Enter the smallest side of the triangle : "))

area = find_area(a,b,c)
print(f"Area of the Triangle is : {area}")