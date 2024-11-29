def most_frequent_element(lst):
    if not lst:
        return None
    freq = {}
    for item in lst:
        if item in freq:
            freq[item]+=1
        else:
            freq[item]=1
    max_freq = max(freq,key=freq.get)
    return max_freq

user_input = list(map(int,input("Enter numbers separated by space : ").split()))
most_freq = most_frequent_element(user_input)
print(f"Most frequent element is {most_freq}")