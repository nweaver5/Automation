import os
from sys import stdout
#from colorama import init
#from termcolor import colored
#init()

path = 'ChromeLogs\\'
listing = os.listdir(path)

print("| Chrome | \n")

numFailsTotal = 0
numFailsBrowser = 0

for infile in listing:
	print("File = " + infile + "\n")
	numFails = 0
	
	with open(path + '\\' + infile, encoding='utf-8') as f:
		f = f.readlines()

	phrase = "Fail"

	for line in f:
		if phrase in line:
			print(line)
			numFails += 1
			numFailsBrowser += 1
			numFailsTotal += 1

	print("Number of Errors in This File: " + str(numFails) + "\n")

print("Number of Errors for Chrome: " + str(numFailsBrowser) + "\n")
print("Total Number of Errors: " + str(numFailsTotal) + "\n")