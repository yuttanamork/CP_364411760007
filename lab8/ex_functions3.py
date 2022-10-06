"""
name: yuttana datmark
id: 364411760007
group: mit421
"""

# functions wiht default parameter
def myfunc(msg = "mit"):
    print("hello<,",msg)

# calling functions with default parbmeter
myfunc()
myfunc("thungsong")

# functions wiht keyword parameter
def myfunc2(num1,num2,num3):
    print(num1,num2,num3)

# calling functions with keyword parbmeter
myfunc2(num3=30,num1=10,num2=20)

# functions with multiplesc keyword parameter
def myfunc3(**data):
    print(data)
    print(data.keys())
    print(data.values())

# key=value
myfunc3(name="mork",major="mit")












