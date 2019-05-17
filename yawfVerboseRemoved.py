#!/usr/bin/python

import argparse
import sys
import requests
import hashlib
import os
import json

def main():
	#Create Parser Obj to get input arguments
	parser = argparse.ArgumentParser(description='Yet Another Web Fuzzing Tool Designed to Brute Force Directories')
	parser.add_argument('-t','--target',  action="store", dest="target", help='Takes in the target url')
	parser.add_argument('-f', '--file', action="store", dest="directoryFile", help='Takes in the file containing directories')
	parser.add_argument('-c', action="store_true", help="Hash the Landing Page and Compare all Subsequent Requests to the Hash.  Ideal for static landing pages")
	parser.add_argument('--verbose', action="store_true", help='Print Verbose Output')
	parser.add_argument('--tor', action="store_true", help='Use Tor To Anonymize Connections')
	parser.add_argument('--version', action='version', version='%(prog)s 2.1')
	
	#Check and Ensure Proper Arguments were passed.  If not, displays help menu
	if len(sys.argv[1:]) == 0:
		parser.print_help()
		parser.exit()
	#Get arguments
	inputs = parser.parse_args()

	#Uses Tor Network to Check Website
	if inputs.tor == True:
		#Starts Tor (if already running tor handles itself)
		os.system("/usr/bin/tor")
		print("You are anonymized")
		
		#Run a request to show exit interface
		session = requests.session()
		session.proxies = {}
		session.proxies['http'] = 'socks5h://localhost:9050'
		session.proxies['https'] = 'socks5h://localhost:9050'
		hostGet = session.get("https://httpbin.org/ip")
		initResponse = hostGet.text
		
		#Parse initResponse to show pretty result
		jsonParse = json.loads(initResponse)
		origin = jsonParse["origin"]
		exitIP = origin.split(',')
		
		#Displays Your Public Address (Should be Tor Node)
		print("Your Exit IP Is: ", exitIP[0])

		#Gather initial request for analysis
		initArray = tor_Request(inputs.target)
		if inputs.c == True :
				verboseCrypt(inputs.target,inputs.directoryFile,initArray,True,inputs.verbose)
		if inputs.c == False:
				verboseNoCrypt(inputs.target,inputs.directoryFile,initArray,True,inputs.verbose)

		#print(tor_Request(inputs.target))
	if inputs.tor == False:
		print("You are not anonymized")
		#Gather initial request for analysis
		initArray = no_Tor(inputs.target)
		if inputs.c == True :
				verboseCrypt(inputs.target,inputs.directoryFile,initArray,False,inputs.verbose)
		if inputs.c == False:
				verboseNoCrypt(inputs.target,inputs.directoryFile,initArray,False,inputs.verbose)

#Make Initial Request without Tor
def no_Tor(url):
		hostGet = requests.get(url)
		initResponse = hostGet.text
		initHash =  hashlib.sha1(initResponse.encode('utf-8')).hexdigest()
		initList = list(initResponse.split('\n'))
		initArray = [initHash,initList]
		return initArray

#Make Initial Requests using Tor
def tor_Request(url):
		session = requests.session()
		session.proxies = {}

		session.proxies['http'] = 'socks5h://localhost:9050'
		session.proxies['https'] = 'socks5h://localhost:9050'

		hostGet = session.get(url)
		initResponse = hostGet.text
		initHash =  hashlib.sha1(initResponse.encode('utf-8')).hexdigest()
		initList = list(initResponse.split('\n'))
		initArray = [initHash,initList]
		return initArray


#Uses a hashing method to test if pages are unique.
def noVerboseCrypt(url,fileName,arrayResults,torCon,verbose):
	if torCon == True :
		session = requests.session()
		session.proxies = {}

		session.proxies['http'] = 'socks5h://localhost:9050'
		session.proxies['https'] = 'socks5h://localhost:9050'

		with open( fileName, 'r') as ins:
			array = []
			for line in ins:
					hostTest = session.get(url +  (line.rstrip('\n')))
					bruteRes = hostTest.text
					statusRes = hostTest.status_code
					bruteHash = hashlib.sha1(bruteRes.encode('utf-8')).hexdigest()
				if verbose:
					#Verbose Results
					print(url + (line.rstrip('\n')) + ' : ' + 'Percent Difference' , perDif , ' : ' , statusRes)
				else:
					#Nonverbose Results
					if bruteHash != arrayResults[0] :
						print(url + (line.rstrip('\n')) + ' : ' + 'Unique Resolve : ', statusRes)
	if torCon == False :
		with open( fileName, 'r') as ins:
			array = []
			for line in ins:
				hostTest = requests.get(url +  (line.rstrip('\n')))
				bruteRes = hostTest.text
				statusRes = hostTest.status_code
				bruteHash = hashlib.sha1(bruteRes.encode('utf-8')).hexdigest()
				if verbose:
					#Verbose Results
					print(url + (line.rstrip('\n')) + ' : ' + 'Percent Difference' , perDif , ' : ' , statusRes)
				else:
					#Nonverbose Results
					if bruteHash != arrayResults[0] :
						print(url + (line.rstrip('\n')) + ' : ' + 'Unique Resolve : ', statusRes)
				

#Compares how similar pages are via a line by line analysis.
def NoCrypt(url,fileName,arrayResults,torCon,verbose):
	if torCon == True :

		session = requests.session()
		session.proxies = {}
		session.proxies['http'] = 'socks5h://localhost:9050'
		session.proxies['https'] = 'socks5h://localhost:9050'

		with open( fileName, 'r') as ins:
			array = []
			for line in ins:
				hostTest = session.get(url +  (line.rstrip('\n')))
				bruteRes = hostTest.text
				statusRes = hostTest.status_code
				#Compare Init Response with Brute Response
				bruteList = list(bruteRes.split('\n'))
				difList = (list(set(arrayResults[1]) - (set(bruteList))))
				difLen = len(difList) * 1.0
				initLen = len(arrayResults[1]) * 1.0
				fracDif = (difLen/initLen)*1.0
				perDif = fracDif * 100.0
				#Print out results
				if verbose:
					#Verbose Results
					print(url + (line.rstrip('\n')) + ' : ' + 'Percent Difference' , perDif , ' : ' , statusRes)
				else:
					#Non Verbose Results
					if perDif > 5.0 :
						print(url + (line.rstrip('\n')) + ' : ' + 'Percent Difference' , perDif , ' : ' , statusRes)

	if torCon == False :
		with open( fileName, 'r') as ins:
			array = []
			for line in ins:
				hostTest = requests.get(url +  (line.rstrip('\n')))
				bruteRes = hostTest.text
				statusRes = hostTest.status_code
				#Compare Init Response with Brute Response
				bruteList = list(bruteRes.split('\n'))
				difList = (list(set(arrayResults[1]) - (set(bruteList))))
				difLen = len(difList) * 1.0
				initLen = len(arrayResults[1]) * 1.0
				fracDif = (difLen/initLen)*1.0
				perDif = fracDif * 100.0
				#Print out results
				if verbose:
					#Verbose Results
					print(url + (line.rstrip('\n')) + ' : ' + 'Percent Difference' , perDif , ' : ' , statusRes)
				else:
					#Non Verbos Results
					if perDif > 5.0 :
						print(url + (line.rstrip('\n')) + ' : ' + 'Percent Difference' , perDif , ' : ' , statusRes)				

if __name__ == "__main__":
	main()