#!/usr/bin/python
import os
import subprocess
import sys
try:
	a=subprocess.check_call('pmi action',shell=True)
except:
	print '''ERROR Install power management interface using the command
sudo apt-get install powermanagement-interface'''
	exit(0)
if len(sys.argv) < 2:
	print '''Atleast one command line argument is required
Usage : gsuspend now
	gsuspend after n 
		 where n is the number of minutes'''
else:
	if sys.argv[1] == 'now' :
		a=os.system("pmi action suspend")
	elif sys.argv[1] == 'after' :
		a=os.system("echo 'pmi action suspend' | at now +"+sys.argv[2]+"minutes")	
