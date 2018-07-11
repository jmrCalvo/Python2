#!/usr/bin/python3
import os
import sys

# Write a script that receives 2 parameters from the console representing a path to a directory on the system and a file name. The script will recursively through the structure of files and folders under the given parameter using os.walk and write the file given as a parameter all sites path you traveled and it's type (FILE, DIRECTORY, UNKNOWN), separated by |. Each path will be written on one line.
fd=open(sys.argv[2],mode="a")
for (root,directories,files) in os.walk(sys.argv[1]):
	for fileName in directories and files and root:
		full_fileName = os.path.join(root,fileName)
		if os.path.isdir(full_fileName) is True:
			full_fileName=full_fileName+" |DiRECTORY\n"
			fd.write(full_fileName)
		else:
			if os.path.isfile(full_fileName) is True:
				full_fileName=full_fileName+" |FiLE\n"
				fd.write(full_fileName)
			else:
				full_fileName=full_fileName+" |UnKNOWN\n"
				fd.write(full_fileName)
