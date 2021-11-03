"""
Module prints out calendars
"""
#from math import floor
"""
Importing floor function
"""


def weekday_name(number: int) -> str:
    """
    Returns a string representing a weekday
    (one of "mon", "tue", "wed", "thu", "fri", "sat", "sun")
    number : an integer in range [0, 6]

    >>> weekday_name(3)
    'thu'
    """
    days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    return days[number]


def weekday(date1: str) -> int:
    """
    Returns an integer representing a weekday
    (0 represents monday and so on)
    Read about algorithm as Zeller's Congruence
    date : a string of form "day.month.year
    if the date is invalid raises AssertionError
    with corresponding message

    >>> weekday("12.08.2015")
    2
    >>> weekday("28.02.2016")
    6
    >>> weekday("29.02.2016")
    0
    >>> weekday("30.02.2016")
    AssertionError('Invalid date')
    >>> weekday("28.10.2020")
    2
    """
    import datetime
    splitted = date1.split('.')
    isvaliddate = True
    try:
        try:
            ans = datetime.datetime(int(splitted[2]), int(
                splitted[1]), int(splitted[0])).weekday()
            return ans
        except ValueError:
            isvaliddate = False
        if not isvaliddate:
            raise AssertionError('Invalid date')

    except AssertionError as err:
        return err


def calendar(mont: int, yea: int) -> str:
    """Returns a string representing a\
    horizontal calendar for the given month and year.

    month : an integer in range [1 , 12]
    year : an integer (strictly speaking the algorithm in weekday
           works correctly only for Gregorian calendar, so year must
           be greater than 1583)
    when arguments are invalid raises AssertionError with corresponding
    message

    >>> print(calendar(8 , 2015))
    mon tue wed thu fri sat sun
                          1   2
      3   4   5   6   7   8   9
     10  11  12  13  14  15  16
     17  18  19  20  21  22  23
     24  25  26  27  28  29  30
     31
    """
    import calendar as cal1
    cal = cal1.TextCalendar()
    ans = cal.formatmonth(yea, mont, 3)
    ans = ans[ans.index("\n")+1:]
    ans = ans.lower()
    ans = ans[:-1:]
    return ans


def transform_calendar(cal1: str) -> str:
    """Returns a modified horizontal -> vertical calendar.

    calendar is a string of a calendar, returned by the calendar()
    function.
    >>> print(transform_calendar(calendar(5, 2002)))
    mon   6 13 20 27
    tue   7 14 21 28
    wed 1 8 15 22 29
    thu 2 9 16 23 30
    fri 3 10 17 24 31
    sat 4 11 18 25
    sun 5 12 19 26
    >>> print(transform_calendar(calendar(8 , 2015)))
    mon   3 10 17 24 31
    tue   4 11 18 25
    wed   5 12 19 26
    thu   6 13 20 27
    fri   7 14 21 28
    sat 1 8 15 22 29
    sun 2 9 16 23 30
    """
    stra = cal1.split('\n')
    ans = [[], [], [], [], [], [], []]
    for seg in stra:
        ans[0].append(seg[:4])
        ans[1].append(seg[4:8])
        ans[2].append(seg[8:12])
        ans[3].append(seg[12:16])
        ans[4].append(seg[16:20])
        ans[5].append(seg[20:24])
        ans[6].append(seg[24:27])
    result = ''
    for line in ans:
        for elem in line:
            el1 = elem
            el1 = el1.replace(' ', '')
            if len(el1) == 0:
                el1 += ' '
            result = result + el1 + ' '
        result = result[:-1:]
        result = result.rstrip()
        result += '\n'
    result = result[:-1:]
    return result


if __name__ == '__main__':
    try:
        print("Type month")
        month = input()
        month = int(month)
        print("Type year")
        year = input()
        year = int(year)
        print("\n\nThe calendar is: ")
        print(calendar(month, year))
    except ValueError as err:
        print(err)
    import doctest
    print(doctest.testmod())
