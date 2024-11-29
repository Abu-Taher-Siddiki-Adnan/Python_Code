list1 = list(map(int,input("Enter the elements of the first list : ").split()))
list2 = list(map(int,input("Enter the elements of the second list : ").split()))

common_element = list(set(list1) & set(list2))
print(f"Common elements from the two list are : {common_element}")