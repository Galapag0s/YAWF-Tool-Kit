# YAWF
Yet Another Web Fuzzing Tool

Do not use this tool for any illegal activity.  This is for research purposes only. 

Designed for Linux with Python3

To Run this Tool ensure Python3 and Tor are installed. (Tor is only needed if you wish to anonymize yourself)

## Install Instructions

clone https://github.com/aturecek/YAWF.git

apt-get install python3

apt-get install tor

pip install -r requirements.txt


## Options For yawf.py 

usage: yawf.py [-h] [-t TARGET] [-f DIRECTORYFILE] [-c] [--verbose] [--tor]
                 [--version]

Yet Another Web Fuzzing Tool Designed to Brute Force Directories

optional arguments:

  -h, --help            
                    
                    show this help message and exit
  
  -t TARGET, --target TARGET
                        
                     Takes in the target url
                        
  -f DIRECTORYFILE, --file DIRECTORYFILE
                       
                     Takes in the file containing directories
                        
  -c                    
                        
                     Hash the Landing Page and Compare all Subsequent
                     Requests to the Hash. Ideal for static landing pages
  -n NUMTHREADS
  	
		     Takes in the number of threads you wish to use
                
  --verbose             
  
                     Print Verbose Output
  
  --tor                 
  
                     Use Tor To Anonymize Connections
  
  --version             
  
                     Show program's version number and exit

  
 ## Versions
 
 1.0 Initial Release
 
                     Created Basic Framework
                     Script could perform hash and statistical based analysis
 2.0 TOR Release
      
                     Added Support for TOR
                     Improved Internal Functions by Removing Redundant Code
                     Improved Script Feedback to Supply more useful data
 3.0 Multi-Thread Release

		     Added Support for Multi-Threading (2 threads)
		     
 3.1 Multi-Thread Update
 			
		     Added Support for User Input in regards to Threads
  
 ## Future Goals

 - Program Script to Learn Cut Off point dynamically
 
 - Add additional fuzzing commands.
 
 - Add user friendly error reporting
