#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        print(int(-number % 10))
        return(int(-number % 10))
    else:
        print(int(number % 10))
        return(int(number % 10))
    # 'int' is used to convert the possibilities of float argument to interger
