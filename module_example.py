# This simple module is used with the modules_and_packages notebook

def add_nums(n):
	print(n + n)

def sub(n):
	print(1000 - n)
	
def mults(n):
	print(n * 2)

def divs(n):
	print(1000000 / n)
	
def main():
	print('this came from the module named module_ex')

# The __name__ == "__main__" function auto-runs all within (here just main())
# upon module execution (i.e. when python module_example.py file is run)
# Note, when module_example is imported into a file, __name__ == "__main__"
# is not called and main() would need to be called explicitily. 
if __name__ == "__main__":
	main()