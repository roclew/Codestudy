"""
输入年月日,看是第几天
"""


import leap_year


def what_day(years, months, day):
    leapyears = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    notleapyears = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = 0
    if months > 1:
        for index in range(1,months):
            if leap_year.leap_year(years):
                days += leapyears[index-1]
            else:
                days += notleapyears[index-1]
    days += day
    print(days)
    return days


def main():

    year = input("年")
    month = input("月")
    day = input("日")
    days_of_month = [[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
                     [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]][leap_year.leap_year(int(year))]
    print(days_of_month)
    what_day(int(year), int(month), int(day))



if __name__ == "__main__":
    main()



