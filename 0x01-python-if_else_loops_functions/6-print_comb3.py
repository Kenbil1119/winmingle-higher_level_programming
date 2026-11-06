#!/usr/bin/python3
for num1 in range(0, 10): # one digit range 0...9
    for num2 in range(num1, 10):
        if num1 == num2:
            continue
        if num1 + 1 == 9 and num2 == 9:
            print(f"{num1}{num2}")
        else:
            print(f"{num1}{num2}", end=', ')
