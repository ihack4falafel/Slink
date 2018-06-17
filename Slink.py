#!/usr/bin/env python
# MIT License
#
# Copyright (c) 2018 Hashim Jawad
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import sys
import time

# colors
W  = '\033[0m'  # white
R  = '\033[91m' # Light Red
B  = '\033[94m' # Light Blue
G  = '\033[92m' # Light Green
O  = '\033[33m' # orange
LG = '\033[37m' # Light Gray

# this is an alternative encoder function if one of the following bad characters [00,01,10,11,f] is found
def AltEncoder(item, FirstAdd, SecondAdd, ThirdAdd):
	for i in list(item):
		if i == '0':
			FirstAdd   += "1"
			SecondAdd  += "1"
			ThirdAdd   += "1"
		elif i == '1':
			FirstAdd   += "1"
			SecondAdd  += "2"
			ThirdAdd   += "1"
		elif i == '2':
			FirstAdd   += "2"
			SecondAdd  += "1"
			ThirdAdd   += "2"
		elif i == '3':
			FirstAdd   += "2"
			SecondAdd  += "2"
			ThirdAdd   += "2"
		elif i == '4':
			FirstAdd   += "3"
			SecondAdd  += "2"
			ThirdAdd   += "2"
		elif i == '5':
			FirstAdd   += "3"
			SecondAdd  += "3"
			ThirdAdd   += "2"
		elif i == '6':
                       	FirstAdd   += "3"
			SecondAdd  += "3"
			ThirdAdd   += "3"
		elif i == '7':
                     	FirstAdd   += "4"
			SecondAdd  += "3"
			ThirdAdd   += "3"
		elif i == '8':
                       	FirstAdd   += "4"
			SecondAdd  += "4"
			ThirdAdd   += "3"
		elif i == '9':
                       	FirstAdd   += "4"
			SecondAdd  += "4"
			ThirdAdd   += "4"
		elif i == 'a':
                       	FirstAdd   += "5"
			SecondAdd  += "4"
			ThirdAdd   += "4"
		elif i == 'b':
                       	FirstAdd   += "6"
			SecondAdd  += "5"
			ThirdAdd   += "3"
		elif i == 'c':
                       	FirstAdd   += "6"
			SecondAdd  += "5"
			ThirdAdd   += "4"
		elif i == 'd':
                       	FirstAdd   += "6"
			SecondAdd  += "6"
			ThirdAdd   += "4"
		elif i == 'e':
                       	FirstAdd   += "6"
			SecondAdd  += "5"
			ThirdAdd   += "6"
		elif i == 'f':
			FirstAdd   += "7"
    			SecondAdd  += "6"
			ThirdAdd   += "5"

	FirstAdd  = [FirstAdd[i:i+2] for i in range(0, len(FirstAdd), 2)]
	SecondAdd = [SecondAdd[i:i+2] for i in range(0, len(SecondAdd), 2)]
	ThirdAdd = [ThirdAdd[i:i+2] for i in range(0, len(ThirdAdd), 2)]
	print VarName + ' += "'+LG+'\\x25\\x4A\\x4D\\x4E\\x55'+W+'" ## and  eax, 0x554e4d4a'
	print VarName + ' += "'+LG+'\\x25\\x35\\x32\\x31\\x2A'+W+'" ## and  eax, 0x2a313235'
	print VarName + ' += "'+LG+'\\x05\\x'+FirstAdd[3]+'\\x'+FirstAdd[2]+'\\x'+FirstAdd[1]+'\\x'+FirstAdd[0]+W+'" ## add  eax, 0x'+FirstAdd[0]+FirstAdd[1]+FirstAdd[2]+FirstAdd[3]
	print VarName + ' += "'+LG+'\\x05\\x'+SecondAdd[3]+'\\x'+SecondAdd[2]+'\\x'+SecondAdd[1]+'\\x'+SecondAdd[0]+W+'" ## add  eax, 0x'+SecondAdd[0]+SecondAdd[1]+SecondAdd[2]+SecondAdd[3]
	print VarName + ' += "'+LG+'\\x05\\x'+ThirdAdd[3]+'\\x'+ThirdAdd[2]+'\\x'+ThirdAdd[1]+'\\x'+ThirdAdd[0]+W+'" ## add  eax, 0x'+ThirdAdd[0]+ThirdAdd[1]+ThirdAdd[2]+ThirdAdd[3]
	print VarName + ' += "'+LG+'\\x2D\\x33\\x33\\x33\\x33'+W+'" ## sub  eax, 0x33333333'
	print VarName + ' += "'+LG+'\\x50'+W+'"                 ## push eax'

# this is default encoder function if none of 8 bytes chuncks have one of the following bad characters [00,01,10,11,f]
def DefaultEncoder(item, FirstAdd, SecondAdd):
	for i in list(item):
		if i == '0':
			FirstAdd   += "0"
			SecondAdd  += "0"
		elif i == '1':
			FirstAdd   += "1"
			SecondAdd  += "0"
		elif i == '2':
			FirstAdd   += "1"
			SecondAdd  += "1"
		elif i == '3':
			FirstAdd   += "2"
			SecondAdd  += "1"
		elif i == '4':
			FirstAdd   += "2"
			SecondAdd  += "2"
		elif i == '5':
		 	FirstAdd   += "3"
			SecondAdd  += "2"
		elif i == '6':
                    	FirstAdd   += "3"
			SecondAdd  += "3"
		elif i == '7':
                       	FirstAdd   += "3"
			SecondAdd  += "4"
		elif i == '8':
                       	FirstAdd   += "4"
			SecondAdd  += "4"
		elif i == '9':
                       	FirstAdd   += "5"
			SecondAdd  += "4"
		elif i == 'a':
                       	FirstAdd   += "5"
			SecondAdd  += "5"
		elif i == 'b':
                       	FirstAdd   += "6"
			SecondAdd  += "5"
		elif i == 'c':
                      	FirstAdd   += "6"
			SecondAdd  += "6"
		elif i == 'd':
                       	FirstAdd   += "7"
			SecondAdd  += "6"
		elif i == 'e':
                       	FirstAdd   += "7"
			SecondAdd  += "7"
	FirstAdd  = [FirstAdd[i:i+2] for i in range(0, len(FirstAdd), 2)]
	SecondAdd = [SecondAdd[i:i+2] for i in range(0, len(SecondAdd), 2)]
	print VarName + ' += "'+LG+'\\x25\\x4A\\x4D\\x4E\\x55'+W+'" ## and  eax, 0x554e4d4a'
	print VarName + ' += "'+LG+'\\x25\\x35\\x32\\x31\\x2A'+W+'" ## and  eax, 0x2a313235'
	print VarName + ' += "'+LG+'\\x05\\x'+FirstAdd[3]+'\\x'+FirstAdd[2]+'\\x'+FirstAdd[1]+'\\x'+FirstAdd[0]+W+'" ## add  eax, 0x'+FirstAdd[0]+FirstAdd[1]+FirstAdd[2]+FirstAdd[3]
	print VarName + ' += "'+LG+'\\x05\\x'+SecondAdd[3]+'\\x'+SecondAdd[2]+'\\x'+SecondAdd[1]+'\\x'+SecondAdd[0]+W+'" ## add  eax, 0x'+SecondAdd[0]+SecondAdd[1]+SecondAdd[2]+SecondAdd[3]
	print VarName + ' += "'+LG+'\\x50'+W+'"                 ## push eax'

def main():
	
	global VarName

	# take shellcode as raw input
	Shellcode = raw_input("Enter your shellcode: ").lower()
	Shellcode = Shellcode.replace("\\x","")
	Shellcode = Shellcode.replace("'","")
	Shellcode = Shellcode.replace('"',"")

	# take shellcode name variable as raw input
	VarName    = raw_input("Enter shellcode variable name: ")
	VarName    = VarName.replace("'","")
	VarName    = VarName.replace('"',"")

	# check the size of user provided shellcode and pad with NOPS if need be
	ShellcodeSize = ''
	ShellcodeSize = [Shellcode[i:i+2] for i in range(0, len(Shellcode), 2)]
	if len(ShellcodeSize) % 4 != 0:
        	print "["+R+"!"+W+"] Shellcode size is not divisible by 4"
		time.sleep(1)
        	NOP = '90'
	
		if ((len(ShellcodeSize))+1) % 4 == 0:
			Shellcode += "90"
			print "["+G+"+"+W+"] Padding shellcode with 1 NOPS.."
			time.sleep(1)		
		elif ((len(ShellcodeSize))+2) % 4 == 0:
			Shellcode += "90"
			Shellcode += "90"
			print "["+G+"+"+W+"] Padding shellcode with 2 NOPS.."
			time.sleep(1)
		else:
			Shellcode += "90"
			Shellcode += "90"
			Shellcode += "90"
			print "["+G+"+"+W+"] Padding shellcode with 3 NOPS.."
			time.sleep(1)
	else:
		print "["+G+"+"+W+"] Shellcode size is divisible by 4"
		time.sleep(1)
		pass

	Shellcode = "".join(reversed([Shellcode[i:i+2] for i in range(0, len(Shellcode), 2)]))

	ShellcodeFormatted = ''	
	ShellcodeFormatted = [Shellcode[i:i+8] for i in range(0, len(Shellcode), 8)]
	FirstAdd    = ""
	SecondAdd   = ""
	ThirdAdd    = ""
	c1 = 0
	c2 = 0
	for item in ShellcodeFormatted:
		print '[' +B+ '*' +W+ '] Encoding [%s]..' %item
		time.sleep(1)
		TwoBytes = [item[i:i+2] for i in range(0, len(item), 2)]
		# if this is true go to AltEncoder
		if any(i == '00' for i in list(TwoBytes)) or any(i == '01' for i in list(TwoBytes)) or any(i == '10' for i in list(TwoBytes)) or any(i == '11' for i in list(TwoBytes)) or any(i == 'f' for i in list(item)):
			time.sleep(1)
                        print '['+R+'!'+W+'] Possible bad character found, using alterantive encoder..'
			AltEncoder(item, FirstAdd, SecondAdd, ThirdAdd)
			c1 += 1
		# if this is true go to DefaultEncoder
		else:
                        print '['+G+'+'+W+'] No bad character found, using default encoder..'
			time.sleep(1)
			DefaultEncoder(item, FirstAdd, SecondAdd)
			c2 += 1

	# calculate shellcode size (bytes)
	ShellcodeFinalSize = ((21 * c2) + (31 * c1))
	print '['+B+'*'+W+'] Shellcode final size: ' + str(ShellcodeFinalSize) + ' bytes'

if __name__ == '__main__':
	main()
