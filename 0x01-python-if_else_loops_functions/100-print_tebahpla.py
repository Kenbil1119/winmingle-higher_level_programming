#!/usr/bin/python3
"""
A program that prints the ASCII alphabet, in reverse order.
Alternating lowercase and uppercase (z in lowercase and Y in uppercase).
Not followed by a new line.
"""
lowercase = 122 # ASCII number of 'z'
uppercase =  89 # ASCII number of 'Y'
while lowercase >= 97: # ASCII number of 'a'
	print(f"{lowercase:c}{uppercase:c}", end='')
	lowercase -= 2
	uppercase -= 2