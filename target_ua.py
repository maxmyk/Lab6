"""
Target_ua
"""


def generate_grid():
    """
    generates grid of five unique letters

    >>> generate_grid()
    ['г', 'ч', 'в', 'е', 'м']
    """
    from random import randint
    alphabet = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
    field = set()
    while len(field) < 5:
        field.add(alphabet[randint(0, len(alphabet)-1)])
    return list(field)


def get_words(file, letters):
    """
    Gets right words
    """
    ans = set()
    with open(file, "r", encoding='utf-8') as file:
        for line in file:
            line = line.lower()
            line1 = line.split()
            if line1[0][0] in letters and len(line1[0]) <= 5:
                if 'noun' in line1[1] or '/n' in line1[1]:
                    ans.add((line1[0], 'noun'))
                elif 'verb' in line1[1] or '/v' in line1[1]:
                    ans.add((line1[0], 'verb'))
                elif 'adj' in line1[1]:
                    ans.add((line1[0], 'adjective'))
                elif 'adv' in line1[1]:
                    ans.add((line1[0], 'adverb'))
                else:
                    pass
    return list(ans)
#print(get_words('base.lst', generate_grid()))


def check_user_words(user_words, language_part, letters, dict_of_words):
    right = []
    for word in user_words:
        if word[0] in letters and len(word[0]) <= 5:
            for elem in dict_of_words:
                if elem[0] == word and elem[1] == language_part:
                    right.append(word)
                    dict_of_words.remove(elem)
    return right, dict_of_words
#print(check_user_words(['край', 'криза'], 'noun', ['з', 'к', 'я', 'п', 'л'], get_words('base.lst', ['з', 'к', 'я', 'п', 'л'])))
