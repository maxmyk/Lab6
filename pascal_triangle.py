"""
Module generates Pascal triangle
"""


def generate_pascal_triangle(num):
    """
    returns pascal triangle
    >>> generate_pascal_triangle(4)
    [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
    >>> generate_pascal_triangle(3)
    [[1], [1, 1], [1, 2, 1]]
    """
    import math
    ans = [[]]
    for j in range(num):
        for i in range(j+1):
            ans[j].append(
                int((math.factorial(j) / (math.factorial(i) * math.factorial(j - i)))))
        ans.append([])
    ans.pop()
    return ans


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
