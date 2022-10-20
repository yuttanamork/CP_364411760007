"""
Name: {yuttana datmark}
SID: {364411760007}
Group: {mit 421}
"""

# Exceptions
print("start")

while True:
   try:
       num = int(input("enter an integer."))
       print(f'your number is {num}')
       break
   except ValueError as e:
       print("error log:",e.args)
       print("please, enter only integer.")



print("end")

