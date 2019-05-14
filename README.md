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
                     
 
 ## Future Goals
 
 - Combine Verbose and No Verbose, Pass verbose as an option to each function
 
 - Don't Show 404 code

 - Add option for multiple threads to increase the speed.
 
 - Program Script to Learn Cut Off point dynamically
 
 - Add additional fuzzing commands.
 
 - Add user friendly error reporting
