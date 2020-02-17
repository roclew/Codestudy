"""
后缀名获取
"""


def get_suffix(filename):
    p = filename.rfind('.')
    if 0 < p < len(filename)-1:
        return filename[p:]
    else:
        return "there is no suffix"


def main():
    print(get_suffix(input()))


if __name__ == "__main__":
    main()
