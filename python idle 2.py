Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']
num1=12.5
type(num1)
<class 'float'>
id(num1)
3176396814960
num1=num1+100
num1
112.5
id(num1)
3176428900720
0007bond="spy"
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
bond007="spy"
Int=1000
Int
1000
help("keywords)
     
SyntaxError: unterminated string literal (detected at line 1)
help("keywords")
     

Here is a list of the Python keywords.  Enter any keyword to get more help.

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not                 

await               finally             nonlocal            yield
SyntaxError: invalid syntax
int
<class 'int'>
int(123.5)
123
int (123.5)
123
int =1000
dir()
['Int', '__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'bond007', 'int', 'num1']
int
1000
int(12.34)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    int(12.34)
TypeError: 'int' object is not callable
del(int)
dir()
['Int', '__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'bond007', 'num1']
del(int)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    del(int)
NameError: name 'int' is not defined. Did you mean: 'Int'?
dir()
['Int', '__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'bond007', 'num1']
int(12.34)
12
num1=0b101
num1
5
num1=0b1111
num1
15
num1=0o123
num1
83
>>> num1=0o128
SyntaxError: invalid digit '8' in octal literal
>>> num1=0o128
SyntaxError: invalid digit '8' in octal literal
>>> num1=oxf
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    num1=oxf
NameError: name 'oxf' is not defined
>>> num1=0xf
>>> num1
15
>>> num1=0xface
>>> num1
64206
>>> num1=0xzoom
SyntaxError: invalid hexadecimal literal
>>> numq=15
>>> bin(num1)
'0b1111101011001110'
>>> numq
15
>>> num1=15
>>> bin(num1)
'0b1111'
>>> oct(num1)
'0o17'
>>> hex(num1)
'0xf'
>>> num1=2e2
>>> num1
200.0
>>> num1=12+5j
>>> num1
(12+5j)
>>> type(num1)
<class 'complex'>
>>> num1=4+2j
>>> num1
(4+2j)
>>> num1.real
4.0
>>> num1.imag
2.0
>>> num1.conjugate()
(4-2j)
>>> c=12j+5
>>> c
(5+12j)
passexam=True
type(pasexam)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    type(pasexam)
NameError: name 'pasexam' is not defined. Did you mean: 'passexam'?
type(passexam)
<class 'bool'>
True==1
True
Fakse==0
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    Fakse==0
NameError: name 'Fakse' is not defined. Did you mean: 'False'?
False==0
True
True>False
True
st="python"
st
'python'
priint(st)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    priint(st)
NameError: name 'priint' is not defined. Did you mean: 'print'?
print(st)
python
type(st)
<class 'str'>
