"""
name: yuttana datmark
id: 364411760007
group: mit421
"""

# functions with multiple parameter
def myfunc(*msg): # *msg ---> tuple (...)
    print(msg)
    print(type(msg))

def myfunc2(*value):
    total = 0
    for x in value:
        total += x
    print(total)
    # print(total)
    return total


myfunc(10)
myfunc(10,20,30)

x = myfunc2(10)
x = myfunc2(11,22,33,44,55)
print(x)









