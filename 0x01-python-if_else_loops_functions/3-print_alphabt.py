#!/usr/bin/python3
# ASCII representation of 'a' - 'z' is from 97 to 122
for letter in range(97, 123):
    if chr(letter) == 'e' or chr(letter) == 'q':
        continue
    print(f"{letter:c}", end='')
