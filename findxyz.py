"""
白鸡问题
"""

x = 0   #公鸡数量
y = 0   #母鸡数量
z = 0   #小鸡数量

for x in range(1,21):
    for y in  range(1,34):
        for z in  range(1,101):
            if x * 5 + y * 3 + z / 3 == 100 and x + y + z == 100:
                print("%d公鸡,%d母鸡,%d小鸡"%(x,y,z))
