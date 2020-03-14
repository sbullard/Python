"""
This example is simple module(basic_math.py) 
inside of a packckage(test_package) directory

This module performs 4 basic math computations
including: addition, subtraction, multication, and division
"""

def sumz(n):
    # Triple quotes must surround any comments if you want
	# to use them in python built-in help() function
	'''
	Returns the summed value n + n
	'''
	print(f'{n} + {n} = {n + n}')

def sub(n):
	print(f'1000 - {n} = {1000 - n}')
	
def mult(n):
	print(f'{n} * {n} = {n * n}')

def divs(n):
	print(f'1000000 / {n} = {1000 / n}')
	
def main():
	print('this is the basic_math module inside of the test_package package')
	
if __name__ == "__main__":
	main()