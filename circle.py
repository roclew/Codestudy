'''
输入半径，计算圆形的面积和周长
'''
import  math

radius = float(input("请输入圆形的半径："))

perimeter = radius * math.pi * 2
print("圆形的周长是 %.3f m"%(perimeter))

area = (radius * radius) * math.pi
print("圆形的面积是 %.4f"%(area))