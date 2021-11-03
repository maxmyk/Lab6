"""
Returns lucky numbers
"""
from typing import List
"""
importing List
"""


def sieve_flavius(num: int) -> List[int]:
    """
    Function returns lucky numbers from 1 to selected number
    int -> lst
    >>> sieve_flavius(25)
    [1, 3, 7, 9, 13, 15, 21, 25]
    >>> sieve_flavius(10)
    [1, 3, 7, 9]
    """
    ans = list(range(1, num + 1))[::2]
    i = 1
    while i < len(ans):
        ans = [ans[j] for j in range(len(ans)) if j % ans[i] + 1 != ans[i]]
        i += 1
    return ans


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
