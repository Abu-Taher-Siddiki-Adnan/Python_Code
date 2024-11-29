myDict={'Name':'Adnan','Age':'22','Height':'5ft 7inch', 'Weight':'78kg'}
key_to_remove = input("Enter the key you want to check : ")

if key_to_remove in myDict:
    value = myDict.pop(key_to_remove)
    print(f"The key '{key_to_remove}' removed with value '{value}' from the dictionary")
    print(f"Updated Dictionary : {myDict}")
else:
    print(f"{key_to_remove} does not exist in the dictionary")