def flatten_nested_list(input_list):
    flattened_list = []
    for item in input_list:
        if isinstance(item,list):
            flattened_list.extend(flatten_nested_list(item))
        else:
            flattened_list.append(item)
    return flattened_list

list1 = [ 2 , 3 , [4 , 5 , [ 6 , 7] ,8 ] , 9 , [ 10 , 11 ] ]
flattened = flatten_nested_list(list1)
print(f"Flattened list : {flattened}")
