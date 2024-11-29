num_list = list(map(int,input("Enter the element of the list : ").split()))
print("1. Sort in ascending order.")
print("2. Sort in descending order.")

option = int(input("Enter the number of the option : "))

if option==1:
    num_list.sort()
    print(f"The sorted list in ascending order is : {num_list}")
else:
    num_list.sort(reverse=True)
    print(f"The sorted list in descending order is : {num_list}")
