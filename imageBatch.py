from __future__ import print_function
from glob import glob
from shutil import move

import os

DESTINATION = 'JPG'

def list_dir():
	print("Finding JPEGs")
	return glob('*.jpg')

def jpg_move(files):
	print("Found: " + str(files))
	print("Checking for destination folder, and creating if needed...")
	#Code to check for the destination directory, and create it if it doesn't exist. This may have bugs on some systems, but it seems to work on my Mac for now.
	if not os.path.exists(DESTINATION):
		print("Oops, didn't find it, attempting to create it")
		os.makedirs(DESTINATION)
		print("Folder created!")
	else:
		print("Found it!")

	for item in files:
		print("Moving " + item)
		move(item, DESTINATION)
	print("Done!")

jpg_move(list_dir())
