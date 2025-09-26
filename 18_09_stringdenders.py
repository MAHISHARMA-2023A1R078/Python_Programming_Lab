print(dir(str))
st="Welcome to the orld of string"

st="Welcome to the world of string"
st.upper() #object new bana pr store nhi lrwaya too collected by garbage colllecctor
print(st)

st="Welcome to the world of string"
st=st.upper() 
st=st.lower()
print(st)


#case manipulation functions:
#captialize function : first letter capital krta ha bs forst word ka in a string
st="welcome to the world of string"
st=st.capitalize() #ATL: #Axtartcion transformartion loading
print(st)

#Title function: to convert every word's first letter to capital
st="welcome to the world of string"
st=st.title() #ATL: #Axtartcion transformartion loading
print(st)


st="welcome to the world of string"
st=st.swapcase()
print(st)

                 #  -------------------#formatting functions:#--------------------------#
name="mahi"
age=18
print("my name is",name,"and i am ",age ,"year's old")
print("mu name is "+name+" and i am "+str(age)+" year's old")
#in c
print("my name is %s and i am %d year's old"%(name,age))
print("my name is {} and i am {} year's old".format(name,age))


emp=[101,"james","james@gmail.com",10]
print("eid:{} name:{} email:{} did:{}".format(emp[0],emp[1],emp[2],emp[3]))

emp=[101,"james","james@gmail.com",10]
print("eid:{} name:{} email:{} did:{}".format(*emp)) #*emp means unpack in a string
# here * is var arg: variable length argument string , 4 curly brackets so vlaues should also be 4 or more than 4 not less than 4


#################################################
name="mahi"
age=18
print("my name is {} and i am {} year's old".format(name,age))
print(f"my name is {name} and i am {age} year's old") # f se pata chlega : ki name and age ke andar values hain : that it's not a string
#so use f before double quotes
####################################################

headings=["eid","name","email","salary","did"]
emp1=[101,"james","james@gmail.com",6000,10]
print("{:<5}{:<15}{:<20}{:<9}{:^}".format(*headings)) #left allign{:<5}, right{:>5} center{:^}
print("-"*60)
print("{:<5}{:<15}{:<20}{:<9}{:^}".format(*emp1)) #left allign{:<5}, right{:>5} center{:^}


headings=["eid "," name "," email "," salary "," did "]
emp1=[101," james "," james@gmail.com ",6000,10]
print("{}{}{}{}{}".format(*headings)) #left allign{:<5}, right{:>5} center{:^}
print("{}{}{}{}{}".format(*emp1)) #left allign{:<5}, right{:>5} center{:^}


headings=["eid","name","email","salary","did"]  #justification: left, right and centre 
emp1=[101,"james","james@gmail.com",6000,10]
print("{:^}{:^15}{:^15}{:<9}{:>12}".format(*headings)) #left allign{:<5}, right{:>5} center{:^}
print("-"*60)
print("{:^}{:<15}{:^15}{:<9}{:>12}".format(*emp1)) #left allign{:<5}, right{:>5} center{:^}

#to centre allign the string:

st="welcome"
print(st.center(40))

st="$15000"
print(st.center(40)) # 40 char space insert krdega empty

st="$15000"
print(st.center(40,'-'))



#for left: ljust [      Allignment         ]
#for right: rjust
#for center: center
st="$15000"
print(st.ljust(40,'-')) # 40 char space insert krdega empty

st="$15000"
print(st.center(40,'-')) # 40 char space insert krdega empty

st="$15000"
print(st.rjust(40,'-')) # 40 char space insert krdega empty


####################
#ENCODE FUNCTION: string encoding to convert a string into binary
st="Python"
bst=st.encode(encoding="ascii", errors="strict") #utf8: universal text format 8 bit
print(bst)
# b repsernts a small b : iits a brinary string not a normal string

st="Python"
bst=st.encode(encoding="ascii", errors="strict") #utf8: universal text format 8 bit
print(bst)
newst=bst.decode(encoding="ascii",errors="strict")
print(newst)


st="Python"
bst=st.encode(encoding="utf8", errors="strict") #utf8: universal text format 8 bit
print(bst)
newst=bst.decode(encoding="utf8",errors="strict")
print(newst)

#strict for error
st="Pyth"+"\u229a"+"n"
print(st)
bst=st.encode(encoding="ascii",errors="strict")
print(bst)
#circle ring operator not in ascii so gives error


#ignore
st="Pyth"+"\u229a"+"n"
bst=st.encode(encoding="ascii",errors="ignore")
print(bst)

#replace 
#error ko replace ki konsa error ha 
st="Pyth"+"\u229a"+"n"
bst=st.encode(encoding="ascii",errors="replace")
print(bst)


#namereplace
st="Pyth"+"\u229a"+"n"
bst=st.encode(encoding="ascii",errors="namereplace") #errors  ke naam: strict, replace, ignore, namereplace
print(bst)


#-------------------------------------------for encryption: iibrary: #lib
pwd="mahi1223"
# encryption ke liye md5 function: in lirary #lib
import hashlib #->gives object in encrypted str
encstr=hashlib.md5(pwd.encode()) #hashlib object 
print(encstr.hexdigest()) #encrupted string mein se string nikal ke dega object string se 
# strings must be encoded before error


#pwd se password match progeam:
pwd="b1a8a273363535b43cc826398866a5be"
import hashlib 
password=input("enter your password")
password=hashlib.md5(password.encode())
print(password.hexdigest())
# ----

# md5 is a function jo  hashlib object mein se encrypted string nikalne ke liye ham hashdigest function  ka use krte ha 

# count function: duplicay find krn mien help
st="mississipi"
print(st.count("s"))

#can pass string sequence as well
st="mississipi"
print(st.count("iss"))

# index 4 se 8 tk kinti bar s aya 4 ke baad #range count 4 se 8 tk 4 inclusive and 8 exclusive
st="mississipi"
print(st.count("s",4,8))

# what is the index of p;
st="mississippi"       # gives first occurance of index 
print(st.index("p"))

#                                  make translation and translate: [masking]
# char ko mask krne mein hide krne mein help krte hain
st="python is a high level language"
# jitne bhi vowels hain unhe specific char ke puche kro hide;
st1="aeiou" #jinkko hide krna ha 
st2="12345" # a ko 1 se,  2 ko b se  and so on
#transition table: which helps in masking (mapping table)
ttab=str.maketrans(st1,st2)
print(ttab) #gives ascii code  of a: 1 and so on
print(st.translate(ttab))


#--------------------------------- make translation and translate: [masking] to-> hide  give space
# char ko mask krne mein hide krne mein help krte hain
st="python is a high level language"
# jitne bhi vowels hain unhe specific char ke puche kro hide;
st1="aeiou" #jinkko hide krna ha 
st2="     " # a ko 1 se,  2 ko b se  and so on
#transition table: which helps in masking (mapping table)
ttab=str.maketrans(st1,st2)
print(ttab) #gives ascii code  of a: 1 and so on
print(st.translate(ttab))


#                                 make translation and translate: [masking] to-> hide  give star
# char ko mask krne mein hide krne mein help krte hain
st="python is a high level language"
# jitne bhi vowels hain unhe specific char ke puche kro hide;
st1="aeiou" #jinkko hide krna ha 
st2="*****" # a ko 1 se,  2 ko b se  and so on
#transition table: which helps in masking (mapping table)
ttab=str.maketrans(st1,st2)
print(ttab) #gives ascii code  of a: 1 and so on
print(st.translate(ttab))

