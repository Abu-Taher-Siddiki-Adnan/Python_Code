fruits = {
    'apple' : '2',
    'banana' : '1',
    'orange' : '3',
    'watermelon' : '2'
}

sorted_dict = dict(sorted(fruits.items(), key = lambda item: item[1]))
print(f"Sorted Dictionary : {sorted_dict}")