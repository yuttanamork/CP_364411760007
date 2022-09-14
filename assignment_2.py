"""
Name: {yuttana datmark}
SID: {364411760007}
Group: {mit 421}
"""

myList = [10,20,30,40,50]

# แสดงผลข้อมูลใน myList ทั้งหมด
print(myList)
print(len(myList))
print(type(myList))

# แสดงผลข้อมูล 20 จาก myList
print(myList[1],type(myList[0]))

# แสดงผลข้อมูล 50 จาก myList
print(myList[4],type(myList[4]))

# แสดงผลข้อมูล 50 จาก myList โดยใช้ negative index
print(myList[-1],type(myList[-1]))

# แสดงผลข้อมูล {20,30,40} โดยใช้ range index
print(myList[1:4])

# แสดงผลข้อมูล {40,50} โดยใช้ range index
print(myList[3:])

# แสดงผลข้อมูล {10,20} โดยใช้ range negative index
print(myList[:-3])

# แสดงผลข้อมูลใน myList ทั้งหมด โดยการใช้ while loop
c = 0
while c < len(myList):
    print(myList[c],end=" ")
    c+=1

# แสดงผลข้อมูลใน myList ทั้งหมด โดยการใช้ for loop
for x in range(len(myList)):
    print(myList[x])

# เพิ่มข้อมูล 100,200,300 ใน myList
myList2 = [100,200,300]
myList = myList + myList2
print(myList)

# เพิ่มข้อมูล 400 ใน myList ในตำแหน่งที่ 0
myList.insert(0,400)
print(myList)

# เพิ่มข้อมูล 500 ใน myList ในตำแหน่งที่ 3
myList.insert(3,500)
print(myList)

# แสดงผลข้อมูลใน myList ทั้งหมด
print(myList,type(myList))

# ลบข้อมูล 10
del myList[1]
print(myList)

# ลบข้อมูล 100
del myList[6]
print(myList)

# แสดงผลข้อมูลใน myList ทั้งหมด
print(myList,type(myList))

# ลบข้อมูลตำแหน่งสุดท้ายใน myList
myList.pop()
print(myList)

# แสดงผลข้อมูลใน myList ทั้งหมด
print(myList,type(myList))

# เรียงข้อมูล myList จาก น้อย-มาก
myList.sort()
print(myList)

# แสดงผลข้อมูลใน myList ทั้งหมด
print(myList,type(myList))

# เรียงข้อมูล myList จาก มาก-น้อย
myList.reverse()
print(myList)

# แสดงผลข้อมูลใน myList ทั้งหมด
print(myList,type(myList))

# comprehension
# คัดลอกข้อมูลใน myList ที่มีค่ามากกว่า 50 มาเก็บไว้ใน newList
newlist = myList.copy()
newlist = [x for x in myList if x>50]
# แสดงผลข้อมูลใน newList ทั้งหมด
print(newlist)

# นำข้อมูลใน mylist และ newList มารวมกัน และเก็บไว้ในตัวแปร myFinalList
myFinalList = myList + newlist
# แสดงผลข้อมูลใน myFinalList ทั้งหมด
print(myFinalList)