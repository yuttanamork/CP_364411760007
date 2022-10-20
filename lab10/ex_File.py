"""
Name: {yuttana datmark}
SID: {364411760007}
Group: {mit 421}
"""

# file I/O

# open file

f = open("test.txt")
print(f.read())
f.close()

f = open("test.txt")
print(f.read(2))
f.close()

f = open("test.txt")
print(f.readline(3))
f.close()

f = open("test.txt")
line = f.readlines()
for x in line:
    print(x)
f.close()

print(line)

count = 1
for x in range(len(line)):
    print(count,line[x])
    if count ==3:
        break
    count += 1
