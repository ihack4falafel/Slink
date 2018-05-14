<p align="center">
  <img  highet=200 width=300 src="https://github.com/ihack4falafel/Slink/blob/master/_Logo_.png">
</p>

# 
Slink is an alphanumeric shellcode (x86) encoder that use simple math operations to reformat characters beyond `7f`. The tool creation was inspired by the following sploit [EDB-ID: 44455](https://exploit-db.com/exploits/44455/). The following are list of current features:

- Encode using `01-7f` characters set.
- Exclude common bad characters by default `\x00\x10\x0a\x0d`.
- Check shellcode size and make sure its divisible by 4, otherwise pad with `\x90`.
- Accept mutiple shellcode formats as input.
- Output encoded shellcode.

Watch Slink in action.

<p align="center">
  <img  src="https://github.com/ihack4falafel/Slink/blob/master/Demo.gif">
</p>
