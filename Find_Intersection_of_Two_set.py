def find_intersection(set1,set2):
    values = set1.intersection(set2)
    return values

input_set1 = input("Enter the elements of first set(separated by space) : ")
input_set2 = input("Enter the elements of second set(separated by space) : ")

set1 = set(map(int,input_set1.split()))
set2 = set(map(int,input_set2.split()))

intersection = find_intersection(set1,set2)
print(f"The intersection of the two sets is : {intersection}")