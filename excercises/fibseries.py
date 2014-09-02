#Fibonacci Series in Python

a,b = 0,1 #multiple assignment in Python

#as in C while loops in Python will terminate with a 0 value which is read as false
while b <1000:
	print b, #Note the comma, with it all output is on same line, without different lines
	a, b = b, a+b