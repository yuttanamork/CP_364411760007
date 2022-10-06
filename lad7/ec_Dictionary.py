"""
name: yuttana datmark
id: 364411760007
group: mit421
"""


# data collection - dictionary
# keys:values

d = {"name":"yuttana","age":23,"major":"mit"}
print(type(d))
print(d)

# access to value to dictionary - using keys
print(d["name"])
print(d["age"])
print(d["major"])
# print(d["uni"])

# get()
print(d.get("name"))
print(d.get("age"))
print(d.get("major"))

# keys()
x = d.keys()
print(x,type(x))
#print(x[0])

# values()
y = d.values()
print(y,type(y))

# items()
z = d.items()
print(z,type(z))

# loop - for
for x in d:
    print(x)
for x in d.keys():
    print(x)
# values
for x in d:
    print(d[x])
for x in d.values():
    print(x)
# items
for x,y in d.items():
    print(x,y)

# vchanging value in dict
print(d)
# mit --> ac
d["major"] = "ac"
print(d)
# upddata()
# 23 --> 26
d.update({"age":26})
print(d)

# daa items to dict
d["university"] = "ruts"
print(d)
d.update({"faculty":"mt"})
print(d)

# remove item in dict
# pop()
d.pop("university")
print(d)
# pop items
d.popitem()
print(d)
# del keysword
if "major" in d:
    del d["major"]
else:
    print("no major key in d")
print(d)

# clear()
d.clear()
print(d)

# copy dictionary
x ={1:100,2:200,3:[3,30,300]}
print(x)

y =x
print(y)
x[1] = 1000
print(x)
print(y)

# copy()
y = x.copy()
print(y)
x[1] = 10
print(x)
print(y)

print(x)
print(x[3][2])




