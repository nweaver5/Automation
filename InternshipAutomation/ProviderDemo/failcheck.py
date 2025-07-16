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
numFailsBrowser = 0

path = 'FirefoxLogs\\'
listing = os.listdir(path)

print("| Firefox | \n")

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

print("Number of Errors for Firefox: " + str(numFailsBrowser) + "\n")
numFailsBrowser = 0

path = 'IntexplorerLogs\\'
listing = os.listdir(path)

print("| Internet Explorer | \n")

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

print("Number of Errors for IE: " + str(numFailsBrowser) + "\n")
numFailsBrowser = 0

path = 'BStackLogs\\'
listing = os.listdir(path)

print("| BrowserStack | \n")

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

print("Number of Errors for BrowserStack: " + str(numFailsBrowser) + "\n")
numFailsBrowser = 0

path = 'SafariLogs\\'
listing = os.listdir(path)

print("| Safari | \n")

for infile in listing:
	print("File = " + infile + "\n")
	numFails = 0

	with open(path + '\\' + infile, encoding='utf-8') as f:
		f = f.readlines()

	phrase = "Fail"

	for line in f:
		if phrase in line:
			print(line)
			#print(colored(line, 'red'))
			numFails += 1
			numFailsBrowser += 1
			numFailsTotal += 1

	print("Number of Errors in This File: " + str(numFails) + "\n")

print("Number of Errors for Safari: " + str(numFailsBrowser) + "\n")
print("Total Number of Errors: " + str(numFailsTotal) + "\n")