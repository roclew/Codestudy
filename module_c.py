"""最小公倍数和最大公约数"""


def gcd(a, b):
    if a >= b:
        (a, b) = (b, a)
    for i in range(a, 0, -1):
        if a % i == 0 and b % i == 0:
            return i


def lcm(a,b):
    return (a*b)//gcd(a,b)


def main():
    print(gcd(int(input("A=")), int(input("B="))))
    print(lcm(int(input("A=")), int(input("B="))))


if __name__ == "__main__":
    main()

