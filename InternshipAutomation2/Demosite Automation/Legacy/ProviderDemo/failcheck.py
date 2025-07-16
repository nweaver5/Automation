import os
import sys
import re

outputFile = ("ProviderDemo\\provider_demosite_errors.log")
output = open(outputFile, 'w', encoding='utf-8')
sys.stdout = output

userProfile = os.environ['USERPROFILE']
path = os.path.dirname(userProfile + '\\Desktop\\Demosite Automation\\ProviderDemo\\ChromeLogs\\')
listing = os.listdir(path)

print("Chrome\n")

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

path = os.path.dirname(userProfile + '\\Desktop\\Demosite Automation\\ProviderDemo\\FirefoxLogs\\')
listing = os.listdir(path)

print("Firefox\n")

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

path = os.path.dirname(userProfile + '\\Desktop\\Demosite Automation\\ProviderDemo\\IntexplorerLogs\\')
listing = os.listdir(path)

print("Internet Explorer\n")

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

path = os.path.dirname(userProfile + '\\Desktop\\Demosite Automation\\ProviderDemo\\BStackLogs\\')
listing = os.listdir(path)

print("BrowserStack\n")

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
print("Total Number of Errors: " + str(numFailsTotal) + "\n")

output.close()
sys.stdout = sys.__stdout__

string = open(outputFile).read()
new_string = re.sub('[^a-zA-Z0-9\n\.]', ' ', string)
open(outputFile, 'w', encoding='utf-8').write(new_string)