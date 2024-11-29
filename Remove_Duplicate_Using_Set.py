def Remove_duplicate(list1):
    return list(set(list1))
user_list = list(map(int,input("Enter numbers separated by space : ").split()))
Removed  = Remove_duplicate(user_list)
print(f"List after removing duplicate : {Removed}")