"""
英寸和厘米的之间的转换
"""

value = float (input("请输入长度数据:"))
unit = input("请输入单位:")
if unit == "厘米" or unit == "cm":
    print("%.4f %s = %.4f 英寸"%(value,unit,value/2.54))
elif unit == "in" or unit == "英寸":
    print("%.4f 英寸 = %.4f 厘米"%(value,value*2.54))
else:
    print("您输入了错误的单位")