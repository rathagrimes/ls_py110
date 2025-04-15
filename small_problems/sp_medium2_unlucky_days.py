# Some people believe that Fridays that fall on the 13th day of the
# month are unlucky days. Write a function that takes a year as an
# argument and returns the number of Friday the 13ths in that year. You
# may assume that the year is greater than 1752, which is when the
# United Kingdom adopted the modern Gregorian Calendar. You may also
# assume that the same calendar will remain in use for the foreseeable
# future.

import datetime

def friday_the_13ths(year):
    thirteenths = [datetime.date(year, m, 13).weekday() for m in range(1, 13)]
    return thirteenths.count(4)



print(friday_the_13ths(1986) == 1)      # True
print(friday_the_13ths(2015) == 3)      # True
print(friday_the_13ths(2017) == 2)      # True
