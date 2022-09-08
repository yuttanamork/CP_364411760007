"""
name: yuttana datmark
id: 364411760007
group: mit421
"""

#list comperhenaion

num = []

for x in range(1,101):
    num.append(x)
print(num)

newlist = [x for x in num if x%3==0]
print(newlist)