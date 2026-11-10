#!/usr/bin/pyhton3
def remove_char_at(str, n):

	"""
	Write a function that creates a copy of the string.
	Removing the character at the position n (not the Python way, the “C array index”).
	"""

	new_str = ''
	for i, c in enumerate(str):
		if i == n:
			continue
		new_str += c
	return new_str