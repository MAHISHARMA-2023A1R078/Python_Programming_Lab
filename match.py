##num=int(input("enter the no of rows"))
##match num:
##    case 1:print("Sunday")
##    case 2:print("Monday")
##    case 3:print("Tuesday")
##    case _:print("default")
##
##char=input("enter a char").lower()
##if(len(char)==1):
##   match char:
##       case 'a':print("vowel")
##       case 'e':print("vowel")
##       case 'i':print("vowel")
##       case 'o':print("vowel")
##       case 'u':print("vowel")
##       case _:print("consonant")
##else:
##    print("invalid char")

##while exp:
##    body
##
##init=0
##while(init<=5):
##    print(init, "hello")
##    init+=1
##
##
##

##while True:
##    print("hello")
##    choice=input("do you want to print it again y/n")
##    if choice=='n':
##        break

import random
num=random.randint(1,100)
init=0
while True:
    no=int(input("enter ur no"))
    init=init+1
    if(no<num):
        print("number too low ")
    elif(no>num):
        print("number too high ")
    else:
        print("u guessed")
        break
print("ending the game in ",init," attempts")
    

    
