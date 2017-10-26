#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, platform, signal
if len(sys.argv) != 2:
	print "Usage: ", __file__, " \"file_been_translated\""
	exit()

from googletrans import Translator as t
import io
t= t()

def interrupt():
	print "Interrupt Break^C"
	exit()
	
signal.signal(signal.SIGINT, interrupt)


print "Prepearing file ", sys.argv[1] 
try:
	f = io.open( sys.argv[1] )
except IOError:
	print "Can't load file ", sys.argv[1]
	exit()

new_filename = 'translated_' + sys.argv[1]
new_file = io.open(new_filename , 'w',)

i = 0
lines = f.readlines()
errors_list = []

# struct for line 
# 1|available|(adjective)| có sẵn\n
# 1|successfull|(adjective)| thành công\n
for line in lines:
	i += 1
	line = line.strip()
	en = line.split("|")[1]
	try:
		vi =  t.translate( en, src='en', dest='vi' ).text
	except Exception as e :
		print e
		vi = ''
		errors_list.append(en)

	print "[ " + str(i) + " ] ", en, ' => ', vi
	new_line = line + '|' + vi + '\n'
	new_file.write(new_line)
new_file.close()

print "============== [ Done ] =============="
print "============ errors list ============="
print errors_list
