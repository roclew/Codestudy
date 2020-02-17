"""
用于找到水仙花数字

"""

for i in range(100,1000):
    z = i % 10
    y = i //10%10
    x = i //100
    if x**3+y**3+z**3 == i:
        print(i)


