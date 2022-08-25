"""
name:yuttana datmark
id:364411760007
group:mit421
"""


# idantity opertors
x = 10
y = 10
z = x
# is
print(f'x is y --> {x is y}')
print(f'x is z --> {x is z}')

s1 = "Hello"
s2 = "Hello"
s3 = "hello"
print(f's1 is s2 -->{s1 is s2}')
print(f's1 is s3 -->{s1 is s3}')

l1 = (1,2,3)
l2 = (1,2,3)
l3 = l1
print(f'l1 is l2 -->{l1 is l2}')
print(f'l1 is l3 -->{l1 is l3}')


# is not
print(f'l3 is not l1 -->{l3 is not l1}')
