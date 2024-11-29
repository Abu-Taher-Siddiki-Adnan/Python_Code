def Remove_duplicate(list1):
   unique_list = []
   for item in list1:
       if item not in unique_list:
           unique_list.append(item)
   return unique_list
user_list = list(map(int,input("Enter numbers separated by space : ").split()))
Removed  = Remove_duplicate(user_list)
print(f"List after removing duplicate : {Removed}")