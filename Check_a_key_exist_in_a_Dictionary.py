myDict={'Name':'Adnan','Age':'22','Height':'5ft 7inch', 'Weight':'78kg'}
key_to_check = input("Enter the key you want to check : ")

if key_to_check in myDict:
    print(f"{key_to_check} exist in the dictionary")
else:
    print(f"{key_to_check} does not exist in the dictionary")