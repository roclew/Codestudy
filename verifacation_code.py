"""
验证码函数
"""

import random


def verifacation_code(code_len = 4):
    ver_code = ""
    for i in range(code_len):
        ver_code += (chr(random.randint(48, 90)))
    print(ver_code)
    return ver_code


if __name__ == "__main__":
    verifacation_code(int(input("几位:")))
