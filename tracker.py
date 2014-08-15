#!/usr/bin/python

import os
import md5
import sys

filename = 'tracker.db'
honeypots = ['honeypot.whatever.com']

def sms(id):
  os.system('python ~/gvoice/sms.py '+number+' "[+] $(date) New TTY log has been created due to a successful login from honeypot: '+id+'"')
#  print '[+] text sent'
  return

try: 
  f = open(filename, 'r+')
except IOError:
  print >> sys.stderr, '[!] Error: file not found- '+filename
  exit()
database = f.read()
try:
  database = database[:-1]
  database = dict(item.split(":") for item in database.split("\n"))
except:
  print >> sys.stderr, '[!] Error: database file is not in the correct format'
  exit()
f.close()

current = {}

for i in honeypots:
  signature = md5.md5(''.join(os.listdir('/path/to/folder'))).digest().encode('hex')
  line = i+':'+signature
  current[i] = signature

#print database
#print current

def updatedb():
  os.remove(filename)
  f = open(filename, 'w+')  
  for i in current.keys():
    f.write(i+':'+current[i]+'\n')

#  f.write(current)
  f.close()

# compare each item to database value

for item in database.keys():
  if item in current:
    #print '[+] '+item+' exists'
    newHash = current[item]
    oldHash = database[item]
    print newHash
    print oldHash
    if newHash == oldHash:
      print '[+] %s: Hashes match' % item
      #do_something()
      pass
    else:
      print '[-] %s: Hashes do not match' % item
      #do_something()
      sms(item)
      pass
  else:
    print '[-] '+item+' does not exist'
updatedb()

