import string
def remove_Punctuation(s):
    newS = s.maketrans(' ',' ',string.punctuation)
    return s.translate(newS)
input_string = input("Enter a string : ")
print(input_string)
print(f"After removing punctuation : {remove_Punctuation(input_string)}")