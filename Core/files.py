
# To open a file for reading it is enough to specify the name of the file:

# f = open("demofile.txt")
# The code above is the same as:

# f = open("demofile.txt", "rt")
# Because "r" for read, and "t" for text are the default values, you do not need to specify them.

# Pythonic way:
# filepath = 'Iliad.txt'
# with open(filepath) as fp:
#    for cnt, line in enumerate(fp):
#        print("Line {}: {}".format(cnt, line))

filepath = ('test.oat')

with open(filepath) as obj:
	for cnt, line in enumerate(obj):
		print('Line {}: {}'.format(cnt, line))


with open(filepath) as obj:
	for line in enumerate(obj):
		str = line[1];
		print(str)
		if str.startswith('Scenario:'):
			print('This is a scenario')