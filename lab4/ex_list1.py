"""
name: yuttana datmark
id: 364411760007
group: mit421
"""

#list = []

mylist =[] # empty list
print(mylist)
print(len(mylist)) # return integer value --> 0


mylist = [10,20,30,40,50]
print(mylist)
print(len(mylist))
print(type(mylist))

# access to meber in list
print(mylist[0], type(mylist[0]))
print(mylist[1])
print(mylist[2])
print(mylist[3])
print(mylist[4])
#print(mylist[5])
#negative index
print(mylist[-1])
print(mylist[-2])
print(mylist[-3])
print(mylist[-4])
print(mylist[-5])
#range index {start:stop}
mylist = [10,20,30,40,50]
#[20,30,40]
print(mylist[1:4])
# [10,20]
print(mylist[0:2])
#[20,30,40,50]
print(mylist[1:6])
#[40,50]
print(mylist[3:])
#range negative index {start:stop}

#[20,30,40]
print(mylist[-4:-1])
# [10,20]
print(mylist[-5:-3])
#[20,30,40,50]
print(mylist[-5:-1])
#[40,50]
print(mylist[-2:])

# loop
# for
for x in mylist:
    print(x, x*10)

for x in range(len(mylist)):
    print(mylist[x])

# while
c = 0 # first index in list
while c < len(mylist):
    print(mylist[x],end=" ")
    c +=1

 
