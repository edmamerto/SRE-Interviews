# Store unique file names from the logs to another file
# A line should only consist of one file name

import re

resultFile = open('output.txt', 'a+')
inputFile = open('access.log', 'r') 

seen = set()

for line in inputFile:
	x = re.search("[a-zA-Z-0-9\._]+\.[a-z]+\s", line)

	if x and x.group() not in seen:
		seen.add(x.group())
		resultFile.write(x.group()+'\n')	