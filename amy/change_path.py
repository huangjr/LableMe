import os
import sys
import fileinput

#FILE_PATH: current working directory
for filename in os.listdir(r'FILE_PATH'):
	if filename.split('.')[1] == 'xml':
		for line in fileinput.input(filename, inplace = 1):
			if 'FileName' in line:
				line = '<SinglePage FileName="FILE_PATH' + line.split('/')[-1]
			sys.stdout.write(line)
				
