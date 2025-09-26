#copy and reverse functions:
lst=["james","neena","blake","neena","anna"]
print(f"before reverse: {lst}")
lst.reverse()
print(f"after reverse:{lst}")

# for gloabal to not change the roiginal list:
#gloabal functions: sorted and reversed
lst=["james","neena","blake","neena","anna"]
print(f"before reverse: {lst}")
result=list(reversed(lst))
# reverse mein list nhi, reverse iterator object milega uske liye agge list lagana pdega to get the result.
print(f"after reverse:{lst}")
print(f"reverse:{result}")

#int float complex bool immutable and list is mutable :
lst1=[10,[100]]
lst2=lst1
print(lst1,lst2)
# print(id(lst1),id(lst2))
lst2[0]=20 #new object will made.
lst2[1].append(200) 
print(lst1,lst2)  #both are pointing to the same object in memeory 

# to preserve the original list:
#shallow copy : immutabe mein no change and mutable mein change 
lst1=[10,[100]]
lst2=lst1.copy()
print(lst1,lst2)
lst2[0]=20 
lst2[1].append(200) 
print(lst1,lst2)  

#deep copy: child list alag se banage a: total isolated object 
import copy # deep copy is a fn of copy module not list 
lst1=[10,[100]]
lst2=copy.deepcopy(lst1)
print(lst1,lst2)
lst2[0]=20 
lst2[1].append(200) 
print(lst1,lst2)  

#######################
lst2=lst1 #interning
lst2=lst1.copy() #shallow copy
lst2=copy.deepcopy(lst1) #deep copy
#######################


#4,5,10,11:
#write a program to perform searching activity using linear search and binary search:
lst = []
n = int(input("no of objects: "))

for i in range(n):
    num = int(input("enter the num: "))
    lst.append(num)

target = int(input("enter the no to search: "))

for i in range(len(lst)):
    if target == lst[i]:
        print(f"element found at index {i}")
        break
else:
    print("element not found!")

     
#binary search:
n=int(input("enter your limit"))
lst=list(map(int,input(f"enter {n} nos sepertad by space ").split(" "))) #string maps to integer phir lst mein cast
print(lst)
lst.sort()
print(lst)
min=0
max=len(lst)-1
num=int(input("enter the no to search"))
while(min<=max):
        mid=(min+max)//2 # float error without //
        if(num==lst[mid]):
             print(f"elemnt found at index {mid}")
             break
        elif(lst[mid]<num):
             min=mid+1
        else:
             max=mid-1
else:
     print("element not found!")



#calculator:
a=int(input("enter the first no"))
b=int(input("enter the second no"))
c=int(input("enter the operator to perform calculation:"))
match c:
     case 1: print(a+b)
     case 2: print(a-b)
     case 3: print(a*b)
     case 4: 
          print(a//b)
          if(b==0):
               print("enter b>0")
     case 5: print(a%b)
     case _: print("Invalid Choice.")
