def is_empty(input_list):
    if not input_list:
        return "You gave an empty list"
    else:
        return "Your list have elements"

list1 = list(map(int,input("Enter the element of your : ").split()))
result = is_empty(list1)
print(result)