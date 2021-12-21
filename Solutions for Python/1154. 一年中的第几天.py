# 1154. 一年中的第几天
# https://leetcode-cn.com/problems/day-of-the-year/

def isRunNian(year:int)->bool:
    if (year %4 == 0 and year %100 != 0) or year % 400 == 0:
        return True
    return False

def get_days_of_month(run_nian, month):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 31
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    elif month == 2:
        if run_nian:
            return 29
        else:
            return 28


class Solution:
    def dayOfYear(self, date: str) -> int:
        year,month,day = map(lambda x:int(x), date.split("-"))
        run_nian = isRunNian(year)

        days_count = 0
        for month_i in range(1, month):
            days_count += get_days_of_month(run_nian, month_i)
        days_count += day
        return  days_count

