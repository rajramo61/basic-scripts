"""
Define a procedure, deep_reverse, that takes as input a list, and returns a new list that is
the deep reverse of the input list.
This means it reverses all the elements in the list, and if any of those elements are lists themselves,
reverses all the elements in the inner list, all the way down.
"""

def deep_reverse(arr):
	if len(arr) == 0:
		return []
	new_array = []
	for input in arr[-1:]:
		if type(input) is list:
			new_array.append(deep_reverse(input))
		else:
			new_array.append(input)
    pass