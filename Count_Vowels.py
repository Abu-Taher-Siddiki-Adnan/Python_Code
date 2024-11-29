def Count_Vowels(s):
    vowels = "aAeEiIoOuU"
    count = 0
    for char in s:
        if char in vowels:
            count +=1
    return count
input_string = input("Enter a string : ")
print(f"Total vowels in {input_string} is : {Count_Vowels(input_string)}")