# List is mutable: can be changed 

# 'james' "james" '''james''' """james""" => string objects belongs to string class

# [12,12,12,23] => list: comma sepetated values in a square bracket

# [12 23 45 67 89] ==> ndarray 
# (12,34,56,78) =>tuple
# {12,23,45,67} => set
# {1:12, 2: 34} => dictionary: key value pair

# two ways of constructing a list:
# 1. list() -> when we want to convert an existing object into list.
# 2. [] -> when we want to create a list from scratch /beginning . or to crete a new list object

# to create an empty list:
lst=list()
lst=[]
print(lst,type(lst))

#to convert string into a list :

st="HELLO"  #string kko idividual strings ke list mein 
lst=list(st)
print(lst)

#to create a new list : list holding the refrence of these string objects 
lst=['H','E','L','L','o']
print(lst)


#jis pr for loop lge too uspr list apply hoti ha for iterable
lst =list(12345) #int is not allowed ; single int is not a sequence: accepts only iiterable / sequence 
print(lst)

lst =list("12345") #int is not allowed ; single int not a sequence ; allpowed beacuse a sequence 
print(lst)

lst=[10,20,30,40,50]
for i in lst:
    print(i, end=" ")


lst=[10,20,30,40,50]
print(lst[:])
print(lst[0:])
print(lst[:5])

print(lst[-4:3]) # for 20 and 30
print(lst[-4:-2])

#last 3 elements:  
print(lst[-3:])



# revrse: step=-1

print(lst[0::1])

print(lst[0::2])

print(lst[0::3])

print(lst[::-1])  # for reverse order

print(lst[3::-2])


#list is an ordered collection:
lst1=[10,20]
lst2=[20,20]
print(lst1==lst2)

lst1=[10,20]
lst2=[10,20]
print(lst1==lst2)