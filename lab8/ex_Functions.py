"""
name: yuttana datmark
id: 364411760007
group: mit421
"""


# functions
# 1. bull-in functions
print("hello , mit421")
s = "ruts"
print(len(s))

# 2. create by owner -- using "def" keyword
def myfunction1():
    print("hello, from functions1.")

def myfunctions2(msg):
    print("hello,from functions2.",msg)

def myfunctions3(num1,num2):
    print("hello, from functions3.")
    # return statement
    return num1+num2

# calling function
myfunction1()

# calling functions with parameter
myfunctions2("ruts")

# calling functions wiht parameter and return statement
rs = myfunctions3(10,10)
print(rs)

print(myfunctions3(20,20))


