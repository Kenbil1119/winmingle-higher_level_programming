#!/usr/bin/python3
def fizzbuzz():
	"""
    This module contains a function that prints the multiple of 3 as 'Fizz'.
    The multiple of 5 as 'Buzz'.
    The multiple of 3 and 5 as 'FzzBuzz'.
    Prints the number if not the multiple of both.
	"""

	for num in range(1, 101):
		if num % 3 == 0:
			print('Fizz', end='')
		if num % 5 == 0:
			print('Buzz', end='')
		if num % 3 and num % 5:	# If not multiple of 3 and 5
			print(num, end='')
		
		if num < 100:
			print(' ', end='')
		else:
			print()
