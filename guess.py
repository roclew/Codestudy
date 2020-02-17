"""

这是一个猜数字的游戏

"""
import  random

answer=random.randint(1,100)
is_right=True
i=0

while is_right:
    n=int(input("第%d猜,请输入数字"%(i+1)))
    if answer==n:
        is_right=False
        print("猜对了!")
    elif answer<n:
        print("猜大了!")
    else:
        print("猜小了")

    i=i+1
    if i==7:
            is_right=False
            if answer!=n:
                print("猜了7次都不对!数字是:%d"%(answer))

