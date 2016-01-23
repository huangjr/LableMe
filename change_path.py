import os
import sys
import fileinput

for filename in os.listdir(r'FILE_PATH'):
	if filename.split('.')[1] == 'xml':
		for line in fileinput.input(filename, inplace = 1):
			if 'FileName' in line:
				line = line.replace('OLD_FILE_PATH','FILE_PATH')
			sys.stdout.write(line)
				