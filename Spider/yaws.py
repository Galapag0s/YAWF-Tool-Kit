#--------------------------------------------------------------------
#
#	Name: Yet Another Web Spider
#
#	Description: A simple web spider that can crawl a web page.
#		     It will also look for username/passwords
#		     embeded within the sites HTML.
#
#	Version: 1.0
#
#---------------------------------------------------------------------

#!/usr/bin/python

from spider import SpiderSite
import argparse
import requests
import os
import sys
import json

#Main Method to run
def main():
	#Create Parser Obj to get input arguments
	parser = argparse.ArgumentParser(description='Yet Another Web Fuzzing Tool Designed to Brute Force Directories')
	parser.add_argument('-t','--target',  action="store", dest="target", help='Takes in the target url')
	parser.add_argument('--verbose', action="store_true", help='Print Verbose Output')
	parser.add_argument('--tor', action="store_true", help='Use Tor To Anonymize Connections')
	parser.add_argument('--version', action='version', version='%(prog)s 3.1')

	#Check and Ensure Proper Arguments were passed.  If not, displays help menu
	if len(sys.argv[1:]) == 0:
		parser.print_help()
		parser.exit()
	#Get arguments
	inputs = parser.parse_args()

	#Create intial list to hold crawl resutls
	crawlResults = []

	#Runs script based on tor or not
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

		#Runs spider script
		spiderTor(inputs.target,crawlResults)

		#Display results
		displayMap(crawlResults)

	if inputs.tor == False:
		#Runs spider script
		spiderNoTor(inputs.target,crawlResults)

		#Dispaly results
		displayMap(crawlResults)

def spiderTor(target,stack):
	print("placeholder")
	#Crawl site with Tor


def spiderNoTor(target,stack):
	print("placeholder")
	#Crawl site without tor

def displayMap(list):
	firstURL = list[0]
	print(firstURL)
	for i in range len(list):
		for x in range list[i].level
			print("-")
		print(list[i].url)
		#Loop

if __name__ == "__main__":
	main()
