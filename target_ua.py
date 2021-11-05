"""
Target_ua
"""


def generate_grid():
    """
    generates grid of five unique letters

    none -> list()
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
    str, list() -> list()
    >>> get_words('base.lst', ['ь', 'и', 'є', 'ї', 'й'])
    [('ирод', 'noun'), ('ирій', 'noun'), ('йняти', 'verb'), ('йог', 'noun'), \
('йога', 'noun'), ('йод', 'noun'), ('йодат', 'noun'), ('йодид', 'noun'), \
('йодил', 'noun'), ('йодит', 'noun'), ('йодль', 'noun'), ('йола', 'noun'), \
('йолоп', 'noun'), ('йомен', 'noun'), ('йон', 'noun'), ('йорж', 'noun'), \
('йот', 'noun'), ('йота', 'noun'), ('йти', 'verb'), ('йтися', 'verb'), \
('євнух', 'noun'), ('єврей', 'noun'), ('євро', 'noun'), ('єгер', 'noun'), \
('єдваб', 'noun'), ('єзуїт', 'noun'), ('єлей', 'noun'), ('ємний', 'adjective'), \
('ємно', 'adverb'), ('єна', 'noun'), ('єнот', 'noun'), ('єпарх', 'noun'), \
('єресь', 'noun'), ('єри', 'noun'), ('єрик', 'noun'), ('єство', 'noun'), \
('єті', 'noun'), ('єхида', 'noun'), ('їда', 'noun'), ('їдало', 'noun'), \
('їдати', 'verb'), ('їдець', 'noun'), ('їдиш', 'noun'), ('їдкий', 'adjective'), \
('їдло', 'noun'), ('їдок', 'noun'), ('їдом', 'adverb'), ('їдуха', 'noun'), \
('їдьма', 'adverb'), ('їжа', 'noun'), ('їжак', 'noun'), ('їзда', 'noun'), \
('їздак', 'noun'), ('їздка', 'noun'), ('їздун', 'noun'), ('їнь', 'noun'), \
('їсти', 'verb'), ('їстки', 'verb'), ('їхати', 'verb'), ('їхній', 'adjective')]
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
    return sorted(list(ans))


def check_user_words(user_words, language_part, letters, dict_of_words):
    """
    Checks if user words are proper and in dictionary
    list(), str, list(), list() -> list(), list()
    >>> check_user_words(['ирод', 'ирій', 'йог', 'йога'], 'noun', \
['ь', 'и', 'є', 'ї', 'й'], [('ирод', 'noun'), ('ирій', 'noun'), \
('йняти', 'verb'), ('йог', 'noun'), ('йога', 'noun'), ('йод', 'noun'), \
('йодат', 'noun'), ('йодид', 'noun'), ('йодил', 'noun'), \
('йодит', 'noun'), ('йодль', 'noun'), ('йола', 'noun'), \
('йолоп', 'noun'), ('йомен', 'noun'), ('йон', 'noun'), ('йорж', 'noun'), \
('йот', 'noun'), ('йота', 'noun'), ('йти', 'verb'), ('йтися', 'verb'), \
('євнух', 'noun'), ('єврей', 'noun'), ('євро', 'noun'), ('єгер', 'noun'), \
('єдваб', 'noun'), ('єзуїт', 'noun'), ('єлей', 'noun'), ('ємний', 'adjective'), \
('ємно', 'adverb'), ('єна', 'noun'), ('єнот', 'noun'), ('єпарх', 'noun'), \
('єресь', 'noun'), ('єри', 'noun'), ('єрик', 'noun'), ('єство', 'noun'), \
('єті', 'noun'), ('єхида', 'noun'), ('їда', 'noun'), ('їдало', 'noun'), \
('їдати', 'verb'), ('їдець', 'noun'), ('їдиш', 'noun'), ('їдкий', 'adjective'), \
('їдло', 'noun'), ('їдок', 'noun'), ('їдом', 'adverb'), ('їдуха', 'noun'), \
('їдьма', 'adverb'), ('їжа', 'noun'), ('їжак', 'noun'), ('їзда', 'noun'), \
('їздак', 'noun'), ('їздка', 'noun'), ('їздун', 'noun'), ('їнь', 'noun'), \
('їсти', 'verb'), ('їстки', 'verb'), ('їхати', 'verb'), ('їхній', 'adjective')])
    (['ирод', 'ирій', 'йог', 'йога'], \
[('йняти', 'verb'), ('йод', 'noun'), ('йодат', 'noun'), \
('йодид', 'noun'), ('йодил', 'noun'), ('йодит', 'noun'), \
('йодль', 'noun'), ('йола', 'noun'), ('йолоп', 'noun'), \
('йомен', 'noun'), ('йон', 'noun'), ('йорж', 'noun'), \
('йот', 'noun'), ('йота', 'noun'), ('йти', 'verb'), \
('йтися', 'verb'), ('євнух', 'noun'), ('єврей', 'noun'), \
('євро', 'noun'), ('єгер', 'noun'), ('єдваб', 'noun'), \
('єзуїт', 'noun'), ('єлей', 'noun'), ('ємний', 'adjective'), \
('ємно', 'adverb'), ('єна', 'noun'), ('єнот', 'noun'), \
('єпарх', 'noun'), ('єресь', 'noun'), ('єри', 'noun'), \
('єрик', 'noun'), ('єство', 'noun'), ('єті', 'noun'), \
('єхида', 'noun'), ('їда', 'noun'), ('їдало', 'noun'), \
('їдати', 'verb'), ('їдець', 'noun'), ('їдиш', 'noun'), \
('їдкий', 'adjective'), ('їдло', 'noun'), ('їдок', 'noun'), \
('їдом', 'adverb'), ('їдуха', 'noun'), ('їдьма', 'adverb'), \
('їжа', 'noun'), ('їжак', 'noun'), ('їзда', 'noun'), \
('їздак', 'noun'), ('їздка', 'noun'), ('їздун', 'noun'), \
('їнь', 'noun'), ('їсти', 'verb'), ('їстки', 'verb'), \
('їхати', 'verb'), ('їхній', 'adjective')])
    """
    right = []
    for word in user_words:
        if word[0] in letters and len(word[0]) <= 5:
            for elem in dict_of_words:
                if elem[0] == word and elem[1] == language_part:
                    right.append(word)
                    dict_of_words.remove(elem)
    return sorted(right), sorted(dict_of_words)


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
