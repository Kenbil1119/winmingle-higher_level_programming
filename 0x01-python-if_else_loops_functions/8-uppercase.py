#!/usr/bin/python3
def uppercase(s):
    uppercase = ""
    for c in s:
        # Check if it is lowercase character
        if ord(c) >= 97 and ord(c) <= 122:
            uppercase += chr(ord(c) - 32) # Change character to uppercase with the different between 'a' - 'A' (97 - 65)
        else:
            uppercase += c
    print("{}".format(uppercase))
