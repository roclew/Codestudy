#计算组合
import module_a
import module_b as mb
module_a.whoami()
mb.whoami()

from module_a import whoami
import  module_c as cmain



print(cmain.gcd(20,13),cmain.lcm(20,17))

def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result = result * i
    return result


#m = int(input("m = "))
#n = int(input("n = "))


#print(factorial(m)//factorial(n)//factorial(m-n))
#print(str(type(factorial(n))))


def roll_dice(*args):
    total = 0
    for val in args:
        total += val
    return total


