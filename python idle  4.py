Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
num1=12.34
int(num1)
12
int(:12.34")
    
SyntaxError: unterminated string literal (detected at line 1)
int("12.34")
    
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    int("12.34")
ValueError: invalid literal for int() with base 10: '12.34'
int("1234")
    
1234
int("0b101")
    
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int("0b101")
ValueError: invalid literal for int() with base 10: '0b101'
int("0b101",2)
    
5
int("0o123",8)
    
83
int("0xF",16)
    
15
float(123)
    
123.0
float("123.45")
    
123.45
float("123")
    
123.0
str(123)
    
'123'
eval("123")
    
123
eval("123.45")
    
123.45
eval("name")
    
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    eval("name")
  File "<string>", line 1, in <module>
    __import__('idlelib.run').run.main(True)
NameError: name 'name' is not defined
eval("'name'")
    
'name'
name=123
    
eval("name")
    
123
eval(12*5+7/3")
     
SyntaxError: unterminated string literal (detected at line 1)
Eval("12+3*6")
     
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    Eval("12+3*6")
NameError: name 'Eval' is not defined. Did you mean: 'eval'?
eval("12+3*2")
     
18
num=100
     
num1=10
     
num1=4
     
print("sum=",num1+num2)
     
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    print("sum=",num1+num2)
NameError: name 'num2' is not defined. Did you mean: 'num1'?
num1=10
     
num2=4
     
print("sum=",num1+num2)
     
sum= 14
print("floor division="num1//num2)
     
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print("exp=",num1**num2)
     
exp= 10000
print("floor division=",num1//num2)
     
floor division= 2
print("hello")
     
hello
print(10//0)
     
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    print(10//0)
ZeroDivisionError: integer division or modulo by zero
a=100
     
a++
     
SyntaxError: invalid syntax
++a
     
100
a=a+1
     
a
     
101
a+=1
     
a
     
102
a-=1
     
a
     
101
a*=10
     
a
     
1010
a=b=cd=10
     
a=b=c=d=10
     
a,b,c,d
     
(10, 10, 10, 10)
a+=b-=2
     
SyntaxError: invalid syntax


a=10
     
b
     
10
20
     
20
a=10
     
b=20
     
c=30
     
a<b<c
     
True
a<b>c
     
False
a=1000
     
id(a)
     
2172780060432
b=a
     
id(b)
     
2172780060432
a is b
     
True
c=1000
     
id(c)
     
2172780060272
a==c
     
True
a is c
     
False
a==b
     
True
a is b
     
True
b is c
     
False
c is b
     
False
a=100
     
b=100
     
a is b
     
True
a=257
     
b=257
     
a is b
     
False
a=-3
     
b=-3
     
a is b
     
True
a=6
     
b=6
     
a iis b
     
SyntaxError: invalid syntax
a is b
     
True
a=-6
     
b=-6
     
a is b
     
False
range from -5 to 256
     
SyntaxError: invalid syntax
a=254
     
b=254
     
c=254
     
a is c
     
True
a is c
     
True
a=-1
     
b=-1
     
c=-1
     
a is c
     
True
a=-1
     
b=-1
     
a is b
     
True
a=0
     
b=0
     
a is b
     
True
a=1000
     
b=1000
     
a is b
     
False
30 in [10,20,30,40]
     
True
"j" in "james"
     
True
"j" in"James"
     
False
num1=2
     
num2=3
     
>>> print(num1&num2)
...      
2
>>> num1|num2
...      
3
>>> num1^num2
...      
1
>>> !num1
...      
SyntaxError: invalid syntax
>>> !(num1)
...      
SyntaxError: invalid syntax
>>> ~num1
...      
-3
>>> ~num2
...      
-4
>>> num1=0
...      
>>> ~(num1)
...      
-1
>>> num1=1
...      
>>> ~(num1)
...      
-2
>>> num1=-1
...      
>>> ~num1
...      
0
>>> num1=-2
...      
>>> ~num1
...      
1
>>> num1=-5
...      
>>> ~num1
...      
4
