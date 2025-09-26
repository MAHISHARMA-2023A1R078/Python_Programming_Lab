#it may contains dfferent types of objects as it is heterogwnous collection:
lst=[12,12.5,12+5j,"james",True,[10,20,30], sum,len]
for i in lst:   #in list we can store both mutable and imutable types of objects, very versatile.
    print(i,type(i))

print(lst[-1]("james")) #fn can apply on this 
print(lst[-2]([1,2,3,4,6]))


#list can grpow and shrink at runtime
lst=[]
print(lst,id(lst))
lst.append(10)
print(lst,id(lst))
lst.append(20)
print(lst,id(lst))
lst.append(30)
print(lst,id(lst))
del(lst[-1])
print(lst,id(lst)) # id is used to show that object is same in the memory for the list, wich is growing and shrinking.
# del(lst[0])
# print(lst,id(lst))


#list of a list:
lst=[[1,2,3],[4,5,6],[7,8,9]]
for cl in lst:
    print(i)


#agr no even : too print* and if odd : print " "
lst=[[1,2,3],[4,5,6],[7,8,9]]
for cl in lst:
    for ele in cl:
        if(ele%2==0):
            print('*',end=" ") # to put space after nos for printing in one line without \n
        else:
            print(" ",end=" ")
    print() # for printing in next line

#
lst=[[1,2,3],[4,5,6],[7,8,9]]
for cl in lst:
    for ele in cl:
        print(ele**2,end=" ")
    print()


#modification in list:
# want index
lst=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(lst)):
    for j in range(len(lst[i])):
        print((i,j),end=" ")
    print()

print(lst)

#
for i in range(len(lst)):
    for j in range(len(lst[i])):
        lst[i][j]=lst[i][j]**2

print(lst)


#int object is not iterable:
lst=[[1,2,3],4,5,6,[7,8,9]]
for i in lst:
    for j in i:  #4 se loop nhi chla skte kyunki iterbale nhi h
        print(j**2,end=" ")    
    print()

#list and normal objects also: use type fn then 
lst=[[1,2,3],4,5,6,[7,8,9]]
for i in lst:
    if type(i)==list:
        for j in i:
            print(j**2,end=" ") 
    else:
        print(i**2,end=" ")   
    print()

# ----------------how to make a dynamic list:-------------------
lst=[]
n=int(input("no of objects"))
for i in range(n):
    num=int(input("enter the num"))
    lst.append(num)
print(lst)

#OR:

lst=[]
n=int(input("no of objects"))
for i in range(n):
    lst.append(int(input("enter the num")))
print(lst)

#har type ke object ko store krne ke liye: eval use instead of int:
lst=[]
n=int(input("no of objects"))
for i in range(n):
    lst.append(eval(input("enter the num"))) # eval can take list of list also 
print(lst)

#functions:---
#---1.APPEND:

lst=list() #empty list.
lst.append("james")
lst.append("king")  #append adds elements at the end of the list.
lst.append("neena")
print(lst)

#---2.INSERT:
# to insert data inbetween james and king using INSERT

lst.insert(1,"paul")
print(lst)    #list can also hold duplicate objects.
lst.insert(1,"paul")
print(lst)

#---3.COUNT:
print(lst.count("paul")) # ocunt the occurance of objects in the list : no of pauls in a list= 2 

#index 2 ke pass kitne paul ha : 1
# nhi chlega
#print(lst.count("paul",2)) #count takes only 1 arhhuemnt in list.

#---4.INDEX: gives first occurrance.
print(lst.index("paul"))

#index 2 ke baad paul kha ha : 2 parhi ha
print(lst.index("paul",2,7)) #last range tk kyunki mutable
print(lst.index("paul",3)) #error.

#-----5.EXTEND: object pure ko lega na ki ek element ko 
lst1=["red","green","blue"]
lst2=["voilet","cyan"]
lst1.append(lst2)
print(lst1)

lst1=["red","green","blue"]
lst2=["voilet","cyan"]
lst1=lst1+lst2  #new object banegea 
print(lst1)


lst1=["red","green","blue"]
lst2=["voilet","cyan"]   #extend mein new object nhi banaega usmein fn mein hi modify krega same object mein hi store hoga 
lst1.extend(lst2)
print(lst1)


#6. Remove: ---------by pop : index ke behalf pe 
lst=list(range(2,11,2))
print(lst)
#remove last elemtn of this list using 1. pop
res=lst.pop() #list can be converted into stack also using pop and push ka kaam krega append 
#pop nikalke return bhi krta ha 
print(f"popped elemnt is {res}")
print(lst)

#pop bydealt removes last element and otherwise indexed value ko
res=lst.pop(1)
print(f"popped elemnt is {res}")
print(lst)

#value ke behalf pr removal: by ----REMOVE
lst=["james","neena","blake","neena"]
lst.remove("neena")
print(lst) # removes 1st occurance

#delete: by ------del
del(lst[0])
print(lst)

#------to remove whole list:use -------CLEAR:
lst.clear()
print(lst)

# ----sort : same type ke objects pr int, float, string 
lst=["james","neena","blake","neena","anna"]
print(f"before sort{lst}")
lst.sort()
print(f"after sort{lst}")


#sort in descending order: reverse mein
lst=["james","neena","blake","neena","anna"]
print(f"before sort{lst}")
lst.sort(reverse=True)
print(f"after sort{lst}")

# sort se issue:
# list customize : previous order nhi milskta : existing list ko modify krta ha sort 
# for no change in original list 
#------SORTED :
lst=["james","neena","blake","neena","anna"]
print(f"before sort{lst}")
res=sorted(lst)
print(f"after sort{lst}")
print(f"after sort{res}")  #dusri new list change hui : original list mein sab same by SORTED

