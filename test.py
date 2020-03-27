import math

# math.

print("Hello world");

print("Hello\tworld")

#A line comment
'''Multi-
line comment'''
print('something')

exec("print('running the string')") #Working!!!!

a = 4
b = 6 
c ='String'
ac = 'concatenation'
d = '7'
print(a,b,c)

#sprint(a+b+c)

print(a+int(d))#sets to int only temporarily

#print (a+d)

name = "Test name"

print(name)

# name = input("Enter name: ")

print('The name is: ' +name)

print(6/4)#double

print(6//4)#int


#power of
print(2**3)

# modulo
print("Modulo 2%3 is: ",2%3)

print('Modulo 5%2 is', 5%2)

print(dir())

if (a==43):
	print('a is 4 - match')
	if(b==6 | a==33):
		print('Nested if is also a match!')
elif(d=="7"):
	print('elif is true')


	# For loops

print('Range(6)')
for i in range(6):
		print(i)

print ('Range(2,10)')
for i in range(2,10):
			print(i)
print('range(4,30,4)')
for i in range (4,30,4):
		print(i)

# While loops

print('while i<10')

i=0;
while i <10:
	print(i)
	i+=1


#Break and continue

print('break and continue')
i=0

while i <=20:
	i+=1
	if(i<=10):
		continue
	print(i)
	print('continue statement worked and skipped first 10 entries of while loop')
	if(i==18):
		break		

# list all inbuilt functions
print(dir(__builtins__))



help(next)


































