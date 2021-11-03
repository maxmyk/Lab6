"""
Returns lucky numbers
"""


def happy_number(number: int) -> bool:
    """checks if number is lucky
    >>> happy_number(1)
    False
    >>> happy_number(10001)
    True
    """
    number = str(number)
    while len(number) < 8:
        number = '0' + number
    first = number[:4]
    second = number[4:]
    ans = False
    first = str(first)
    second = str(second)
    first = eval(first[0]+'+'+first[1]+'+'+first[2]+'+'+first[3])
    second = eval(second[0]+'+'+second[1]+'+'+second[2]+'+'+second[3])
    if first == second:
        ans = True
    return ans


def count_happy_numbers(num: int) -> int:
    """counts lucky numbers from 0 to n and returns number of
    lucky numbers
    >>> count_happy_numbers(1)
    0
    >>> count_happy_numbers(10001)
    1
    """
    reult = 0
    for i in range(1, num+1):
        if happy_number(i):
            reult += 1
    return reult


def happy_numbers(start1: int, end1: int) -> list:
    """Returns lucky numbers from start1 to end1 and returns number of
    lucky numbers
    >>> happy_numbers(10001,20001)
    [10001, 10010, 10100, 11000]
    >>> happy_numbers(10001, 20005)
    [10001, 10010, 10100, 11000, 20002]
    """
    reult = []
    for i in range(start1, end1+1):
        if happy_number(i):
            reult.append(i)
    return reult


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
