# Strings

a = '#helloButton'
b = 'world'

print (a+' '+b)

c = 54

print(a+str(c))

print(a.upper())

print(a.startswith('h'))

print(a[2])

print(a)

ab = a[1:]

print(ab)

print(a[:1]*5)

 # Lists

list1 = ['hi', '#there', 'yall', 'extra', '#words']

print(list1)

print(list1[1:3])
list1[2] = 'YO!'

print(list1)

print(list1[-1])

list1.append('appended')

for i in list1:
	print(i)

d = list1.count('#') #need to find contains function in the list

print(d)

for i in list1:
	if i.startswith('#'):
		print (i[1:])

# print all created variables

print(dir())



# Tuples - same as lists, but are immutable

tup1 = ('ert',45,'hey', 45, '543')

# Only two functions available

print(tup1.count(45))

print(tup1.index(45))

# Dictionaries

dict1 = {"Sam":12, 'Margaret':55, 'Joe':32}

# add value

dict1['Taty']=33

dict1[99]="Great!"


print(dict1)
dict2 = {"Firtst 5":[1,2,3,4,5], 3:['Sam',45]}

print(dict2)


