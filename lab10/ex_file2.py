"""
Name: {yuttana datmark}
SID: {364411760007}
Group: {mit 421}
"""

# create file
import os

try:
    f = open("C:\\Users\LabCom_MT-4\Desktop\\test3.txt","x")
    f.close()
except Exception as e:
    print(e)


# write file
# mode "a"

try:
    f = open("tast2.txt","w")
    f.write("yuttana datmark\n")
except:
    print("cloud not found a fine name 'test2.txt")
finally:
    f.close()

if os.path.exists("test3.txt"):
    os.remove("test3.txt")
else:
    print("file not found.")
