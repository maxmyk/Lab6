"""
Reads file from url and either returns it or writes into a csv file
"""
from typing import List


def read_input_file(url: str, number: int) -> List[List[str]]:
    """
    (str, int) -> (list(list))
    Preconditions: 0 <= number <= 77

    Return list of strings lists from url

    >>> read_input_file('https://raw.githubusercontent.com/anrom7/\
Test_Olya/master/New%20folder/total.txt',1)
    [['1', 'Мацюк М. І.', '+', '197.859', '10.80']]
    >>> read_input_file('https://raw.githubusercontent.com/anrom7/\
Test_Olya/master/New%20folder/total.txt',3)
    [['1', 'Мацюк М. І.', '+', '197.859', '10.80'], ['2', 'Проць О\
. В.', '+', '197.152', '11.60'], ['3', 'Лесько В. О.', '+', '195.385', '10.60']]
    """
    import urllib.request
    file = urllib.request.urlopen(url)
    ans = []
    i = 0
    for line in file:
        if number == 0 and any(ans):
            ans.pop()
            break
        decoded_line = line.decode("utf-8")
        ssp0 = decoded_line.split()[0]
        if any(ans) and len(ans[i]) == 5:
            i += 1
            number -= 1
        elif ssp0 == '—':
            ans[i].insert(2, decoded_line.split()[1])
        elif 'Середній бал документа про освіту' in decoded_line:
            ans[i].append(decoded_line.split()[-1])
        try:
            if int(ssp0) > 0:
                ans.append([decoded_line.split()[0], decoded_line.split()[1
                ]+' '+decoded_line.split()[2]+' '+decoded_line.split()[3
                ], decoded_line.split()[6]])
        except ValueError:
            pass
    return ans


def write_csv_file(url: str):
    """
    uses read_input_file(url, -1) to get all data and write it into csv file
    """

    filea = open("total.csv", "w", encoding='utf-8')
    filea.rea
    filea.write('№,ПІБ,Д,Заг.бал,С.б.док.осв.\n')
    for line in read_input_file(url, -1):
        ans = ''
        for elem in line:
            ans = ans + ',' + elem
        ans = ans[1::]
        filea.write(ans+'\n')
    filea.close()


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
