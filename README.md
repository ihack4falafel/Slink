<p align="center">
  <img  highet=150 width=150 src="https://github.com/ihack4falafel/Slink/blob/master/_Logo_.png">
</p>

# 
Slink is an alphanumeric shellcode (x86) encoder that use simple math operations to reformat characters beyond `7f`. The tool creation was inspired by the following sploit [EDB-ID: 44455](https://exploit-db.com/exploits/44455/). Here's the list of current features:

- Encode using `01-7f` characters set.
- Exclude common bad characters such as `\x00\x10\x0a\x0d\x20` by default.
- Make sure shellcode is divisible by 4 by padding with `\x90`.
- Accept mutiple shellcode formats as input.
- Specify shellcode variable name.
- Output encoded shellcode.
- Output shellcode final size.


The following demo shows Slink in action.

<p align="center">
  <img  src="https://github.com/ihack4falafel/Slink/blob/master/Demo.gif">
</p>

```
Chanelog:
=========
Version 1.1 (June 2018)
-----------------------
- Add the ability to specify shellcode variable. 
- Add final shellcode size.
- Bug fixes.
- Code optimazation.

Version 1.0 (April 2018)
-----------------------
Initial release!
```
