"""
斐波拉契数列
"""
a = 1
b = 1
c = 0
i = 0

print("1,\t1,",end="\t")

while i < 18:
    c = b + a
    a = b
    b = c
    print("%d,"%(c),end="\t")
    i=i+1




