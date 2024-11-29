def count_frequency(str):
    freq = {}
    for ch in str:
        if ch != ' ':
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1
    return freq

input_string = input("Enter a string : ")
frequency = count_frequency(input_string)
print(f"Frequency of each character : {frequency}")