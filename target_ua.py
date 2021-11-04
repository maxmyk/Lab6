"""
Target_ua
"""
def generate_grid():
    """
    generates grid
    """
    from random import randint
    alp = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
    field = set()
    while len(field) < 5:
        field.add(alp[randint(len(alp))])
    return field

def get_words(file, letters):
    """
    Gets right words
    """
    ans = []
    with open(file, "r", encoding='utf-8') as file:
        for line in file:
            line1 = line.split()
            for word in line1:
                if word[0] in letters and len(line1[0]) <= 5:
                    if 'noun' in word or '/n' in word:
                        ans.append((line1[0], 'noun'))
                    elif 'verb' in word or '/v' in word:
                        ans.append((line1[0], 'verb'))
                    elif 'adj' in word:
                        ans.append((line1[0], 'adjective'))
                    elif 'adv' in word and not 'advp' in word:
                        ans.append((line1[0], 'adverb'))
                    else: break
    return ans