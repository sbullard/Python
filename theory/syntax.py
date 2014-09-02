#python comment

#NOTE - no semi-colons are needed at the end of python statements

print ("Hello World") #print statement
#input statement x = (raw_input("ask user question here"))

#math operators +,-,*,/,%, **
print "3^2 = " , 3 ** 2 ##square root

#boolean true/false
print "5 is > 2 ",5 > 2
print "2 is > 5 ",2 > 5

#variable declarations do not need types
cars = 2
print "I own ", cars, " cars."

#formatting characters
name = "Paul"
last = "My last name is %s"
age = 36
print "My first name is %s" %name
print last % "Bullard"
print "My name is %s Bullard and I am %d years old" %(name,age)

#String concatentation
print "Hello " + "World!"
print "Hello"  " World!" #two strings in quotes next to each other are auto-concatenated
print 3 * ("Hello " + "World! ") #prints 3 versions of the string

#escape characters
print 'C:\Some\name' #here \n means new line
print r'C:\Some\name' #r creates a raw string which prints the whole thing out
print 'doesn\'t' #backslash escape character

#Strings are char arrrays just like in other languages and can be manipulated as such
#NOTE - Strings are IMMUTABLE
word = "Python"
print word[0] + word [1] #first two chars in the word string
print word[-2] + word[-1] #negative numbers are used to start at the end of the array
print word[0:4] #slicing is used to get substrings

#Lists - Similar to List in Java 
squares = [1,4,9,16,25]
print squares
print squares[2]
print squares[:] #creates a shallow copy of the original list 
print squares + [36, 49,64] #can concatenate lists

squares[0] = 100 #Lists are MUTABLE
print squares

squares.append(9 ** 2)
squares[0] = 1
print squares

squares[1:4] = [99,99,99] #slice and replace inner list
print squares

list_a = ['a','b','c'] #nesting lists inside of a list
list_b = [1,2,3]
list_c = [list_a,list_b]
print list_c

#if-Statements 
#Note: Inedention is key in Python, leading whitespace can cause errors
x = int(raw_input("Plese enter an integer: "))

if x < 0:
	x = 0
	print 'Negative changed to zero'
elif x == 0:
	print 'Zero'
elif x == 1:
	print 'Single'
else:
	print 'More'

#for-Statements
#Python for loops iterate over the items of any sequence(list/string), in the order that they appear in the sequence
verbage = ['snake', 'hay', 'bluegrass']
for word in verbage:
	print word, len(word)
#in order to modify a list, a copy needs to be made, use slice to do so
for word in verbage[:]:
	if len(word) > 6:
		verbage.insert(0, word)
		
print verbage		




