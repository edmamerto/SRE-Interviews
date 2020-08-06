# Store unique file names from the logs to another file
# A line should only consist of one file name

import re

resultFile = open('output.txt', 'a+')
inputFile = open('access.log', 'r') 

seen = set()

for line in inputFile:
	x = re.search("[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+", line)

	if x and x.group() not in seen:
		seen.add(x.group())
		# resultFile.write(x.group()+'\n')	
		print x.group()