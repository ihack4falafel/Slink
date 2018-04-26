# Slink
Slink is an Alphanumeric shellcode (x86) encoder that reformat characters beyond `7f` using simple math operations. It also make sure not to generate common bad characters such as `\x00\x0a\x0d`. The tool was heavily inspired by the following exploit [EDB-4445](https://exploit-db/exploits/44455/).

# Usage
Insert your shellcode in line `243` and make sure it can be split to 8 byte chuncks by padding with '\x90' if needed.

# Demo
![alt text](https://github.com/ihack4falafel/Slink/blob/master/PoC.gif)
