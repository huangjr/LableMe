import os
import sys
import fileinput

for filename in os.listdir(r'/Users/jr/Downloads/amy'):
	if filename.split('.')[1] == 'xml':
		for line in fileinput.input(filename, inplace = 1):
			if 'FileName' in line:
				line = '<SinglePage FileName="/Users/jr/Downloads/amy/' + line.split('/')[-1]
			sys.stdout.write(line)
				