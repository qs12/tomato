import glob

listy = glob.glob('**/*.oat', recursive=True)#picks everything from the exec.py file folder and down
# ['2.txt', 'sub/3.txt']

print('\n\nThe list of files:\n\n\n', listy,'\n')

scenarioSteps = ''

for i in listy:
	# print(i)
	filepath = (i)
	linesCount = 0
	with open(filepath) as file:
		for row in file:
			linesCount+=1
	linecount = 0
	with open(filepath) as obj:
		print ('\n', i)
		scenarioSteps = ''
		for line in obj:
			linecount +=1
			if line.startswith('Scenario'):
				scenarioTitle = line;
				print(scenarioTitle)
			elif line in ['\n', '\r\n']:
				strList = scenarioSteps.split()
				print(strList)
				scenarioSteps = ''
			elif linecount==linesCount:
				scenarioSteps += line
				strList = scenarioSteps.split()
				print(strList)
				print('Last line!!!!!!!')

			else:
				scenarioSteps += line

				
				# if str.startswith('Scenario:'):
			# 	print('This is a scenario')