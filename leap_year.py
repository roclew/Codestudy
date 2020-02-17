"""
判断一个年份是否是闰年
"""


def leap_year(years):
    is_leap = (years % 4 == 0 and years % 100 !=0) or (years % 400 == 0)
    if is_leap:
        print("%d 是闰年" % years)
    else:
        print("%d不是闰年" % years)
    return is_leap

