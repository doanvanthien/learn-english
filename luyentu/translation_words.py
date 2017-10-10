

if len(sys.argv) !=2 :
	print "Usage: ", __file__, " argv"
	exit()

print "Loading .... "
from translate import translator
import sys

print "Prepearing translate file ", 'words/' + sys.argv[1], 

t = translator(to_lang='en')

new_file = open('words/' + sys.argv[1] , 'w')

with open('words_raw/' + sys.argv[1]) as f:
	for line in f.readlines():
		en = line.split("|")[1]
		



