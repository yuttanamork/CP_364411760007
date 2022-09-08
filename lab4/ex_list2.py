"""
name: yuttana datmark
id: 364411760007
group: mit421
"""

# list
mylist = [10,20,30,40,50]
# add member to list
# append()
print(mylist)
# add 60 to mylist
mylist.append(60)
print(mylist)

mylist2 = [100,200,300]
mylist.extend(mylist2)
print(mylist)

mylist = mylist + mylist2
print(mylist)

# insert member to list
# insert (indax.data)
mylist.insert(-3,400)
print(mylist)

# app 100 to first member
mylist.insert(0,1000)

# delete member in list
# remove()
mylist.remove(100)
print(mylist)

if 500 in mylist:
    mylist.remove(500)
else:
    print("list has on 500.")
print(mylist)
# pop

# del last membar
mylist.pop()
print(mylist)

mylist.pop(0)
print(mylist)
# del
# del first membar
del mylist[0]
print(mylist)

#del mylist2
print(mylist2)

# change data in list
mylist[-1] = 2000
print(mylist)
mylist[0] = mylist[0]*100
print(mylist)

# sarting data in list
mylist2 = mylist
# sort()
mylist.sort()
print(mylist)

mylist.sort(reverse=True)
print(mylist)

# reverse()
print(mylist2)

# COPY
Newlist = mylist.copy()

mylist.append("mit421")
print(mylist)

print(Newlist)