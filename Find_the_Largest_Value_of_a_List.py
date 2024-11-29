def second_large(num):
    unique_num = list(set(num))
    if len(unique_num) < 2:
        return "'The list does not have second large number'"
    unique_num.sort(reverse=True)
    return  unique_num[1]

num_list = list(map(int,input("Enter the element of a list : ").split()))
number = second_large(num_list)
print(f"The second large number is : {number}")