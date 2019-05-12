#!/usr/bin/python

import argparse
import sys
import requests
import hashlib
import os

def main():
	#Create Parser Obj to get input arguments
	parser = argparse.ArgumentParser(description='Yet Another Web Fuzzing Tool Designed to Brute Force Directories')
	parser.add_argument('-t','--target',  action="store", dest="target", help='Takes in the target url')
	parser.add_argument('-f', '--file', action="store", dest="directoryFile", help='Takes in the file containing directories')
	parser.add_argument('-c', action="store_true", help="Hash the Landing Page and Compare all Subsequent Requests to the Hash.  Ideal for static landing pages")
	parser.add_argument('--verbose', action="store_true", help='Print Verbose Output')
	parser.add_argument('--tor', action="store_true", help='Use Tor To Anonymize Connections')
	parser.add_argument('--version', action='version', version='%(prog)s 2.1')

	if len(sys.argv[1:]) == 0:
		parser.print_help()
		parser.exit()
	#Get arguments
	inputs = parser.parse_args()

	if inputs.tor == True:
		os.system("/usr/bin/tor")
		print("You are anonymized")

		session = requests.session()
		session.proxies = {}
		session.proxies['http'] = 'socks5h://localhost:9050'
		session.proxies['https'] = 'socks5h://localhost:9050'
		hostGet = session.get("https://httpbin.org/ip")
		initResponse = hostGet.text
		print("Your Exit IP Is: ", initResponse)

		initArray = tor_Request(inputs.target)
		if inputs.verbose == True and inputs.c == True :
				verboseCrypt(inputs.target,inputs.directoryFile,initArray,True)
		if inputs.verbose == False and inputs.c == True :
				noVerboseCrypt(inputs.target,inputs.directoryFile,initArray,True)
		if inputs.verbose == True and inputs.c == False:
				verboseNoCrypt(inputs.target,inputs.directoryFile,initArray,True)
		if inputs.verbose == False and inputs.c == False:
				noVerboseNoCrypt(inputs.target, inputs.directoryFile,initArray,True)

		#print(tor_Request(inputs.target))
	if inputs.tor == False:
		print("You are not anonymized")
		initArray = no_Tor(inputs.target)
		if inputs.verbose == True and inputs.c == True :
				verboseCrypt(inputs.target,inputs.directoryFile,initArray,False)
		if inputs.verbose == False and inputs.c == True :
				noVerboseCrypt(inputs.target,inputs.directoryFile,initArray,False)
		if inputs.verbose == True and inputs.c == False:
				verboseNoCrypt(inputs.target,inputs.directoryFile,initArray,False)
		if inputs.verbose == False and inputs.c == False:
				noVerboseNoCrypt(inputs.target, inputs.directoryFile,initArray,False)


def no_Tor(url):
		hostGet = requests.get(url)
		initResponse = hostGet.text
		initHash =  hashlib.sha1(initResponse.encode('utf-8')).hexdigest()
		initList = list(initResponse.split('\n'))
		initArray = [initHash,initList]
		return initArray

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

def verboseCrypt(url,fileName,arrayResults,torCon):
	if torCon == True :
		session = requests.session()
		session.proxies = {}
		session.proxies['http'] = 'socks5h://localhost:9050'
		session.proxies['https'] = 'socks5h://localhost:9050'

		with open(fileName, 'r') as ins:
			array = []
			for line in ins:
				hostTest = session.get(url +  (line.rstrip('\n')))
				bruteRes = hostTest.text
				statusRes = hostTest.status_code
				bruteHash = hashlib.sha1(bruteRes.encode('utf-8')).hexdigest()
				if bruteHash != arrayResults[0] :
					print(url + (line.rstrip('\n')) + ' : ' + 'Unique Resolve : ', statusRes)
				else:
					print(url + (line.rstrip('\n')) + ' : ' + 'Nothing New : ', statusRes)

	if torCon == False :
		with open( fileName, 'r') as ins:
			array = []
			for line in ins:
				hostTest = requests.get(url +  (line.rstrip('\n')))
				bruteRes = hostTest.text
				statusRes = hostTest.status_code
				bruteHash = hashlib.sha1(bruteRes.encode('utf-8')).hexdigest()
				if bruteHash != arrayResults[0] :
					print(url + (line.rstrip('\n')) + ' : ' + 'Unique Resolve : ', statusRes)
				else:
					print(url + (line.rstrip('\n')) + ' : ' + 'Nothing New : ', statusRes)


def noVerboseCrypt(url,fileName,arrayResults,torCon):
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
				if bruteHash != arrayResults[0] :
					print(url + (line.rstrip('\n')) + ' : ' + 'Unique Resolve : ', statusRes)


def verboseNoCrypt(url,fileName,arrayResults,torCon):
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
				#Print out all results
				print(url + (line.rstrip('\n')) + ' : ' + 'Percent Difference' , perDif , ' : ' , statusRes)

	if torCon == False:
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
				#Print out all results
				print(url + (line.rstrip('\n')) + ' : ' + 'Percent Difference' , perDif , ' : ' , statusRes)


def noVerboseNoCrypt(url,fileName,arrayResults,torCon):
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
				if perDif > 5.0 :
					print(url + (line.rstrip('\n')) + ' : ' + 'Percent Difference' , perDif , ' : ' , statusRes)


if __name__ == "__main__":
	main()
