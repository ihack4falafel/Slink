# Slink
Slink is an Alphanumeric shellcode (x86) encoder that reformat characters beyond `7f` using simple math operations. It also make sure not to generate common bad characters such as `\x00\x0a\x0d`. This tool was inspired by the following exploit [EDB-ID: 44455](https://exploit-db.com/exploits/44455/).

# Usage
Insert your shellcode in line `169` in the code and make sure it can be split into 8 byte chuncks by padding with `\x90` if needed.

# Demo
![alt text](https://github.com/ihack4falafel/Slink/blob/master/PoC.gif)
