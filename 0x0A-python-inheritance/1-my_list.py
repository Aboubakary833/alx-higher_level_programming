#!/usr/bin/python3

"""MyList module"""

class MyList(list):
	"""MyList

	Args:
		list (list): Native list
	"""
	def print_sorted(self):
		"""print_sorted
		"""
		print('[', end="")
		for i in range(len(self)):
			if (i == len(self) - 1):
				print("{:d}]".format(sorted(self)[i]))
			else:
				print("{:d}, ".format(sorted(self)[i]), end="")
