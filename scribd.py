import string
import random
import re
import os
from os import path, remove


filesampah = "file__" + str(''.join(random.choice(string.letters+string.digits) for x in range(6))) + ".txt"
basepath = "/home/febrifahmi/Documents/01_CODING/scribd/"

def nyampah(size=5, chars=string.letters+string.digits):
	return ''.join(random.choice(chars) for x in range(size))

# check if any .txt file exist in current dir
for i in os.listdir(basepath):
	if os.path.isfile(os.path.join(basepath,i)) and "file__" in i:
		founditem = os.path.join(basepath,i)
		print "========================================================="
		print "File: " + str(founditem) + " found!. Deleting file......"
		print "---------------------------------------------------------"
		os.remove(founditem)

makeamess = open(filesampah,'w')
nyampahnih = nyampah(size=15000, chars=string.letters+string.digits)
makeamess.write(nyampahnih)
makeamess.close()

print nyampahnih
