# ==============================================================================#
#-- Project Name: Caesars : Moving files
#-- Task : Moves all the file from the directory and makes directeries with 5000 files in each.  
#-- Version : 1.0
#-- Date : 2016:01:13
#-- Author : Neeraj Komuravalli
# ==============================================================================#

#-------------------
# Package imports
#-------------------
import glob
import shutil
import os
import sys

#-------------
# Main code.
#-------------
if len(sys.argv) == 2:
	print "Path is entered"
else:
	print "Pease enter the path"

file_path = sys.argv[1] 

os.chdir(file_path)

i = 0
g = 1
for file in glob.glob("*.jpg"):
	if i == 0:
		dir = "dir_" + str(g)
		os.makedirs(dir)
		g = g + 1
	if i <= 5000:
		shutil.move(file, dir)
		i = i + 1
		if i == 5000:
			i = 0
