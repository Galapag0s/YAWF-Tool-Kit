#!/usr/bin/python

import argparse
import sys
import requests
import hashlib

#Create Parser Obj to get input arguments
parser = argparse.ArgumentParser(description='Yet Another Web Fuzzing Tool Designed to Brute Force Directories')
parser.add_argument('-t','--target',  action="store", dest="target", help='Takes in the target url')
parser.add_argument('-f', '--file', action="store", dest="directoryFile", help='Takes in the file containing directories')
parser.add_argument('-c', action="store_true", help="Hash the Landing Page and Compare all Subsequent Requests to the Hash.  Ideal for static landing pages")
parser.add_argument('--verbose', action="store_true", help='Print Verbose Output')
parser.add_argument('--version', action='version', version='%(prog)s 1.0')

#Check if no arguments were supplied
#If no arguements, show useage and end
if len(sys.argv) < 2:
	parser.print_usage()
	sys.exit(1)

#If arguments Begin parsing so that they can be used
inputs = parser.parse_args()

#Send a GET request to the target
hostGET = requests.get(inputs.target)
initResponse = hostGET.text

#Create Hash for Comparision
initHash =  hashlib.sha1(initResponse.encode('utf-8')).hexdigest()

#Create Set For Comparision
initList = list(initResponse.split('\n'))

#Below Funcitons Send out GET request and then compare results

#Define Funciton For Verbosity with Hash
def verboseCrypt(url,fileName):
	with open( fileName, 'r') as ins:
		array = []
		for line in ins:
			hostTest = requests.get(url +  (line.rstrip('\n')))
                	bruteRes = hostTest.text
                	statusRes = hostTest.status_code
               		bruteHash = hashlib.sha1(bruteRes.encode('utf-8')).hexdigest()
	                if bruteHash != initHash:
                        	print url + (line.rstrip('\n')) + ' : ' + 'Unique Resolve : ', statusRes
			else:
				print url + (line.rstrip('\n')) + ' : ' + 'Nothing New : ', statusRes

#Define Funciton For No Verbosity
def noVerboseCrypt(url,fileName):
        with open( fileName, 'r') as ins:
                array = []
                for line in ins:
                        hostTest = requests.get(url +  (line.rstrip('\n')))
                        bruteRes = hostTest.text
                        statusRes = hostTest.status_code
                        bruteHash = hashlib.sha1(bruteRes.encode('utf-8')).hexdigest()
                        if bruteHash != initHash:
                                print url + (line.rstrip('\n')) + ' : ' + 'Unique Resolve : ', statusRes

#Define Funciton for Verbosity with no Hash
def verboseNoCrypt(url,filename):
	with open( filename, 'r') as ins:
                array = []
                for line in ins:
                        hostTest = requests.get(url +  (line.rstrip('\n')))
                        bruteRes = hostTest.text
                        statusRes = hostTest.status_code
			#Compare Init Response with Brute Response
			bruteList = list(bruteRes.split('\n'))
			difList = (list(set(initList) - (set(bruteList))))
			difLen = len(difList) * 1.0
			initLen = len(initList) * 1.0
			fracDif = (difLen/initLen)*1.0
			perDif = fracDif * 100.0
			#Print out all results
			print url + (line.rstrip('\n')) + ' : ' + 'Percent Difference' , perDif , ' : ' , statusRes

def noVerboseNoCrypt(url,filename):
	with open( filename, 'r') as ins:
                array = []
                for line in ins:
                        hostTest = requests.get(url +  (line.rstrip('\n')))
                        bruteRes = hostTest.text
                        statusRes = hostTest.status_code
                        #Compare Init Response with Brute Response
                        bruteList = list(bruteRes.split('\n'))
                        difList = (list(set(initList) - (set(bruteList))))
                        difLen = len(difList) * 1.0
                        initLen = len(initList) * 1.0
                        fracDif = (difLen/initLen)*1.0
                        perDif = fracDif * 100.0
			#Print out results
			if perDif > 5.0 :
				print url + (line.rstrip('\n')) + ' : ' + 'Percent Difference' , perDif , ' : ' , statusRes


#Run Based on Verbosity and Hash
if inputs.verbose == True and inputs.c == True :
	verboseCrypt(inputs.target,inputs.directoryFile)
if inputs.verbose == False and inputs.c == True :
	noVerboseCrypt(inputs.target,inputs.directoryFile)
if inputs.verbose == True and inputs.c == False:
	verboseNoCrypt(inputs.target,inputs.directoryFile)
if inputs.verbose == False and inputs.c == False:
	noVerboseNoCrypt(inputs.target, inputs.directoryFile)
