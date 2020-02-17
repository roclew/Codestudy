
"""
提供让整数各位的置换
并且说明有多少位
"""

k = int(input("请输入需要换位的数字:"))
j = 0

while True :
    j = j+1
    if k//(10**j) == 0:
        break
jj = j
m = 0
n = 0
p = 0

while True :
    m = k //(10**(j-1))
    k = k % (10**(j-1))
    n = n + m*(10**p)
    j = j - 1
    p = p + 1
    if  j == 0:
        break

print("\n\n输入的数字有%d位\n置换后数字为%d"%(jj,n))