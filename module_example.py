# This is simple module but explains __name__ == "__main__"
# It is used in the modules_and_packages notebook

def add_nums(n):
	print(n + n)

def sub(n):
	print(1000 - n)
	
def mults(n):
	print(n * 2)

def divs(n):
	print(1000000 / n)
	
# All code inside of the main() function will execute ONLY when 
# the module_ex.py file is run and NOT if is imported in another file
def main():
	print('this came from the module named module_ex')

#this code says if you are running this file, then run the main function above
if __name__ == "__main__":
	main()