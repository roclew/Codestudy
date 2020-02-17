"""
用于循环的联系
"""

i = int(input("请输入起始数据:"))
k = int(input("请输入结束数据:"))
j = 0
m = i
is_end = True

while is_end:
    j+=i
    i=i+1
    if i == k+1:
        is_end = False
print("到%d的总和是%d"%(k,j))
print(is_end)

j = 0
for x in range(m,k+1):
    j = x + j
    print(x,j)

print("从%d到%d的总和是%d"%(m,k,j))