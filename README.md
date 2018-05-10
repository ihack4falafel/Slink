<p align="center">
  <img  highet=200 width=300 src="https://github.com/ihack4falafel/Slink/blob/master/Logo.png">
</p>

# 
Slink is an Alphanumeric shellcode (x86) encoder that reformat characters beyond `7f` using simple math operations. This tool was inspired by the following exploit [EDB-ID: 44455](https://exploit-db.com/exploits/44455/). The following are list of current and future features:

- [x] Encode using `01-7f` characters set.
- [x] Execuled common bad characters by default `\x00\x10\x0a\x0d`.
- [x] Check shellcode size and make sure its divisable by 4, otherwise pad with `\x90`.
- [x] Accepet mutiple shellcode formats as input.
- [ ] Output encoded shellcode.

# Demo
<p align="center">
  <img  src="https://github.com/ihack4falafel/Slink/blob/master/PoC.gif">
</p>
