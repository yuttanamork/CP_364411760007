"""
Name: {yuttana datmark}
SID: {364411760007}
Group: {mit 421}
"""

""
"ให้นักศึกษาเขียนตารางสูตรคูณลงในไฟล์ test3.txt"
"โดยการรับ input"
"แม่สูตรคูณจากผู้ใช้มา1ตัวเลข"
""
n = int(input("ใส่ตัวเลข"))

try:
    f = open("C:\\Users\LabCom_MT-4\Desktop\\test3.txt","a")
    for x in range(1,13):
        f.write(f'{n} x {n} = {n*x}\n')
except:
    print("cloud not found a file")
finally:
    f.close()
    print("done")







