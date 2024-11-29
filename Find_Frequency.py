user_list = list(map(int,input("Enter numbers separated by space : ").split()))
element_count = {}
for element in user_list:
    if element in element_count:
        element_count[element] +=1
    else:
        element_count[element] = 1
for element,count in element_count.items():
    print(f"Element {element} occurs {count} times")