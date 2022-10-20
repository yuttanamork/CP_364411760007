"""
Name: {yuttana datmark}
SID: {364411760007}
Group: {mit 421}
"""

print("start")
def divsion(a,b):
    try:
        return a/b
    except:
        raise ZeroDivisionError("division by zero")
try:
    rs = divsion(10,0)
    print("the result: ",rs)
except Exception as e:
    print("errorlog:",e.args)


print("end")