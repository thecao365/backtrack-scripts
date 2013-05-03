#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# By Lee Baird
# Feel free to contact me via chat or email with any feedback or suggestions that you may have:
# leebaird@gmail.com
#
# I'm in the process of totally rewriting this script in Python specifically for Kali.
# I'm brand new to Python, so please bare with me.
#
# Special thanks to the following people:
#
# Ben Wood - regex kung foo
# JK - Python and constant ribbing
# Rob Clowser - Python
#
##############################################################################################################

import getpass
import os
import subprocess
import sys
import time
import urllib2
import webbrowser

# variables
colorblue = "\033[01;34m{0}\033[00m"
colorgreen = "\033[01;32m{0}\033[00m"
colorpurple = "\033[01;35m{0}\033[00m"
colorred = "\033[01;31m{0}\033[00m"
coloryellow = "\033[01;33m{0}\033[00m"
line = "======================================"
user = getpass.getuser()

##############################################################################################################

def banner():
     print
     print "______  ___ ______ ______  _____  _    _ ______  _____"
     print "|     \  |  |____  |      |     |  \  /  |_____ |____/"
     print "|_____/ _|_ _____| |_____ |_____|   \/   |_____ |    \_ Kali"
     print
     print "By Lee Baird"
     print
     print

##############################################################################################################

def cidr():
     print "CIDR"
     goodbye()

##############################################################################################################

def error():
     print
     print
     print colorred.format(line)
     print
     print colorred.format("   *** Invalid choice or entry. ***   ")
     print
     print colorred.format(line)
     time.sleep(2)
     main()

##############################################################################################################

def goodbye():
     print
     print
     print "Coming soon..."
     print
     print
     sys.exit(0)

##############################################################################################################

def lan():
     print "LAN"
     goodbye()

##############################################################################################################

def listener():
     print "Metasploit Listener"
     goodbye()

##############################################################################################################

def lists():
     print "List"
     goodbye()

##############################################################################################################

def main():
     while True:
          choice = menu()
          if choice == "1":
               recon()
          elif choice == "2":
               pingsweep()
          elif choice == "3":
               single()
          elif choice == "4":
               lan()
          elif choice == "5":
               lists()
          elif choice == "6":
               cidr()
          elif choice == "7":
               execfile("multitabs.py")
          elif choice == "8":
               nikto()
          elif choice == "9":
               sslcheck()
          elif choice == "10":
               subprocess.call("/opt/scripts/crack-wifi.sh")
          elif choice == "11":
               reinstall_nmap()
          elif choice == "12":
               listener()
          elif choice == "13":
               sys.exit(0)
          elif choice == "99":
               updates()
          else:
               error()

##############################################################################################################

def menu():
     os.system('clear')
     banner()
     print colorblue.format("RECON")
     print "1.  Scrape"
     print
     print colorblue.format("DISCOVER")+" - Host discovery, port scanning, service enumeration and OS"
     print "identification using Nmap, Nmap scripts and Metasploit scanners."
     print "2.  Ping Sweep"
     print "3.  Single IP, URL or Range"
     print "4.  Local Area Network"
     print "5.  List"
     print "6.  CIDR Notation"
     print
     print colorblue.format("WEB")
     print "7.  Open multiple tabs in Firefox"
     print "8.  Nikto"
     print "9.  SSL Check"
     print
     print colorblue.format("MISC")
     print "10. Crack WiFi"
     print "11. Reinstall nmap"
     print "12. Start a Metasploit listener"
     print "13. Exit"
     print
     return raw_input("Choice: ")

##############################################################################################################

def nikto():
     print "Nikto"
     goodbye()

##############################################################################################################

def pingsweep():
     print "Pingsweep"
     goodbye()

##############################################################################################################

def recon():
     os.system('clear')
     banner()
     print colorblue.format("RECON")
     print
     print "1.  Company"
     print "2.  Person"
     print "3.  Previous menu"
     print
     choice = raw_input("Choice: ")

     if choice == "1":
          scrape()

     if choice == "2": 
          runlocally()
          print
          print line
          print

          firstname = raw_input("First name: ")
          if firstname == "":
               error()
          print
          lastname = raw_input("Last name: ")
          if lastname == "":
               error()

          webbrowser.open('http://www.123people.com/s/'+firstname+'+'+lastname)
          time.sleep(1)
          webbrowser.open('http://www.411.com/name/'+firstname+'-'+lastname)
          time.sleep(1)
          webbrowser.open('http://www.cvgadget.com/person/'+firstname+'/'+lastname)
          time.sleep(1)
          webbrowser.open('http://www.peekyou.com/'+firstname+'_'+lastname)
          time.sleep(1)
          webbrowser.open('http://phonenumbers.addresses.com/people/'+firstname+'+'+lastname)
          time.sleep(1)
          webbrowser.open('http://search.nndb.com/search/nndb.cgi?nndb=1&omenu=unspecified&query='+firstname+'+'+lastname)
          time.sleep(1)
          webbrowser.open('http://www.spokeo.com/search?q='+firstname+'+'+lastname+'&s3=t24')
          time.sleep(1)
          webbrowser.open('http://www.zabasearch.com/query1_zaba.php?sname='+firstname+'%20'+lastname+'&state=ALL&ref=$ref&se=$se&doby=&city=&name_style=1&tm=&tmr=')

          main()

     if choice == "3":
          main()
     else: 
          error()

##############################################################################################################

def reinstall_nmap():
     print "Reinstall nmap."
     goodbye()

##############################################################################################################

def runlocally():
     if not sys.stdout.isatty():
          print
          print line
          print
          print "This option must be run locally, in an X-Windows environment."
          time.sleep(2)
          main()

##############################################################################################################

def scanname():
     typeofscan()

     name = raw_input("Name of scan: ")

     # Check for no answer
     if name == "":
          error()

     os.makedirs("/"+user+"/"+name)

##############################################################################################################

def scrape():
     os.system('clear')
     banner()
     print colorblue.format("RECON")
     print
     print "1.  Passive"
     print "2.  Active"
     print "3.  Previous menu"
     print
     choice = raw_input("Choice: ")

     if choice == "1":
          print
          print line
          print
          print "Usage: target.com"
          print
          domain = raw_input("Domain: ")

          # Check for no answer
          if domain == "":
               error()

          print
          print line
          print

          # If folder doesn't exist, create it
          if not os.path.exists("/"+user+"/"+domain):
               os.makedirs("/"+user+"/"+domain)

          # Number of tests
          total = 28

          print "goofile                   (1/$total)"

          ##############################################################

          runlocally()

          webbrowser.open('https://www.arin.net')
          time.sleep(1)
          webbrowser.open('http://toolbar.netcraft.com/site_report?url=http://www.'+domain)
          time.sleep(1)
          webbrowser.open('http://uptime.netcraft.com/up/graph?site=www.'+domain)
          time.sleep(1)
          webbrowser.open('http://www.shodanhq.com/search?q='+domain)
          time.sleep(1)
          webbrowser.open('http://www.jigsaw.com/')
          time.sleep(1)
          webbrowser.open('http://pastebin.com/')
          time.sleep(1)
          webbrowser.open('http://www.google.com/#q=filetype%3Axls+OR+filetype%3Axlsx+site%3A'+domain)
          time.sleep(1)
          webbrowser.open('http://www.google.com/#q=filetype%3Appt+OR+filetype%3Apptx+site%3A'+domain)
          time.sleep(1)
          webbrowser.open('http://www.google.com/#q=filetype%3Adoc+OR+filetype%3Adocx+site%3A'+domain)
          time.sleep(1)
          webbrowser.open('http://www.google.com/#q=filetype%3Apdf+site%3A'+domain)
          time.sleep(1)
          webbrowser.open('http://www.google.com/#q=filetype%3Atxt+site%3A'+domain)
          time.sleep(1)
          webbrowser.open('http://www.sec.gov/edgar/searchedgar/companysearch.html')
          time.sleep(1)
          webbrowser.open('http://www.google.com/finance/')
          goodbye()

     if choice == "2": 
          print "Active - Coming soon..."
          goodbye()

     if choice == "3":
          main()
     else: 
          error()

##############################################################################################################

def single():
     print "Single"
     goodbye()

##############################################################################################################

def sslcheck():
     print "SSLcheck"
     goodbye()

##############################################################################################################

def typeofscan():
     colorblue.format("Type of scan:")
     print
     print "1.  External"
     print "2.  Internal"
     print "3.  Previous menu"
     print
     choice = raw_input("Choice: ")

     if choice == "1":
          print
          coloryellow.format("[*] Setting source port to 53.")
          sourceport = 53
          print
          print line
          print

     if choice == "2":
          print
          coloryellow.format("[*] Setting source port to 88.")
          sourceport = 88
          print
          print line
          print

     if choice == "3":
          main()
     else: 
          error()

##############################################################################################################

def updates():
     print "Updates"
     goodbye()

##############################################################################################################

main()
