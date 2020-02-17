"""
完美数
"""

i =  8128

for i in range(1,20001):
    k = 0
    for j in range(1,i):
        if i % j == 0:
            k = k + j

    if i == k:
        for j in range(1,i):
            if i % j == 0:
                if j == 1:
                    print(j,end="")
                else:
                    print("+%d"%(j),end="")
        print("=%d"%(i))
