# YAWF
Yet Another Web Fuzzing Tool

Do not use this tool for any illegal activity.  This is for research purposes only. 

Options For yawf.py 

usage: yawf.py [-h] [-t TARGET] [-f DIRECTORYFILE] [-c] [--verbose] [--version] 

Yet Another Web Fuzzing Tool Designed to Brute Force Directories

optional arguments:

  -h, --help            show this help message and exit
  
  -t TARGET, --target TARGET
                        Takes in the target url
                        
  -f DIRECTORYFILE, --file DIRECTORYFILE
                        Takes in the file containing directories
                        
  -c                    Hash the Landing Page and Compare all Subsequent
                        Requests to the Hash. Ideal for static landing pages
                        
  --verbose             Print Verbose Output
  
  --version             show program's version number and exit

-t, --target
            TARGET should be in the form of http(s)://[url]/
            
-f, --file
            DIRECTORYFILE should point to the file you wish to use.
            System will take in text files with one directory/file per line.
            
 -c         Hashes the response from the supplied URL and uses it to compare all subsequent requests.
            This option works best for completely static pages.
            If the target site has a more dynamic landing page, do not use this options.  
            Without this options, the script will review the HTML and find what percent of the page is different.
            Script will report all responses that are 5% different.
            
  --verbose Prints all responses, whether they are identical to the intial landing page, or not. 
  
  
 Future Goals
 
 Add option for multiple threads to increase the speed
 
 Allow uses to specifcy difference cut off point
 
 Add additional fuzzing commands
