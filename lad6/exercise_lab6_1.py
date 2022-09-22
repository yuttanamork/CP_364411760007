"""
Name: {yuttana datmark}
SID: {364411760007}
Group: {mit 421}
"""

"""
เขียนโปรเเกรมเพื่อรับค่าอินพุดจากผู้ใช้เป็นตัวเลขจำนวนเต็ม
จำนวน 2 ชุดข้อมูล โดยมีข้อมูลชุดละ 10 ตัว
จากนั้นให้เเสดงข้อมูลที่ซ้ำกัน เเละไม่ซ้ำกันจากข้อมูล 2 ชุดนี้
ทางจอภาพ
"""
s1 = set()
for i in range(10):
    x = int(input(f"enter an integer {i+1}: "))
    s1.add(x)
print(s1)
s2 = set()
for i in range(10):
    y = int(input(f"enter an integer {i+1}: "))
    s2.add(y)
print(s2)


s4 = s1.intersection(s2)
print(s4)
s5 = s1.symmetric_difference(s2)
print(s5)