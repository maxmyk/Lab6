from typing import List

def sieve_flavius(n: int) -> List[int]:
    if n == 0:
        return []
    if n == 1:
        return [1]
    bool_list = [True]
    bool_list *= (n+1)
    for i in range(1, n+1):
        if i %2==0:
            bool_list[i] = False
    for i in range(3, n+1):
        if bool_list[i] == True:
            ind = 0
            for j in range(1, n + 1):
                if bool_list[j] == True:
                    ind+=1
                if ind % i == 0:
                    bool_list[j] = False
    lucky_list = []
    for i in range(1, n+1):
        if bool_list[i] == True:
            lucky_list.append(i)
    return lucky_list
print(sieve_flavius(100))