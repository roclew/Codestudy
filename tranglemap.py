"""
用*号打印三角形
"""

for i in range(1,6):
    for j in range(1,i+1):
        print("*",end="")
    print()

print()

for i in  range(1,6):
    for j in range(1, 6-i):
        print(" ",end="")
    for k in range(1, i+1):
        print("*",end="")
    print()
