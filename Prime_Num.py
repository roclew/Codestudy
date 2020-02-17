"""
找100以内质数
"""

i = 0
j = 0

print("1\t2",end = "\t")

for i in range(3,10001):
    pr = True
    for j in range(2,i):
        if i % j == 0:
            pr = False
    if pr == True:
        print(i,end="\t")