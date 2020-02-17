"""
计算判断三条线是否能够组成三角形
并计算面积和周长
"""

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
if  a + b > c and b + c > a and c + a > b :
    d = a + b + c
    s = (d/2*(d/2-a) *(d/2-b)*(d/2-c))**0.5
    print("三角形的周长是%.2f,三角形的面积是%.2f"%(d,s))
else:
    print("abc不能构成三角形")