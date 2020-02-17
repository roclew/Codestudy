    # 赌博游戏

from random import  randint

money = 1000
j = 0

while money > 0:
    j = j + 1
    while True:                                         #下注并判断下注金额对不对,不对要求重新下注
        debt= int(input("你还有%d元\n请下注:"%(money)))
        if debt <= money and  debt > 0:
            break
        else:
            print("\n下注金额不对\n")

    a = int(randint(1,6))                              #第一把结果
    b = int(randint(1,6))
    i = 1
    t = a + b
    print("第%d局,第%d把,第一个%d,一个%d,总共%d"%(j,i,a,b,t))
    if t == 7 or t == 11 :                             #第一把开7或者11,玩家赢
        money = money + debt
        print("玩家赢了%d"%debt)

    elif t == 3  or t == 2 or t == 12:
        money = money - debt
        print("庄家赢,玩家输掉%d"%(debt))


    while True:                                        #开始第二把规则
        a = int(randint(1, 6))
        b = int(randint(1, 6))
        i = i + 1
        tt= a + b
        print("第%d局,第%d把,第一个%d,一个%d,总共%d" % (j, i, a, b, tt))
        if tt == 7:
            money = money - debt
            print("庄家赢,玩家输掉%d" % (debt))
            break
        elif tt == t:
            money = money + debt
            print("玩家赢了%d" % debt)
            break

print("你已经输光了!")


