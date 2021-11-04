from typing import List

def generate_grid() -> List[List[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """
    from random import randint
    grid = [[]]
    for i in range(3):
        for _ in range(3):
            grid[i].append(chr(randint(97, 122)))
        grid.append([])
    return grid


def get_words(file: str, letters: List[str]) -> List[str]:
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    """
    from collections import Counter
    words = set()
    file = 'en'
    filea = open(file, "r", encoding='utf-8')
    with open(file, "r", encoding='utf-8') as file:
        for line in filea:
            line = line.lower()
            line = line.strip()

            if len(line) >= 4 and letters[4] in line:
                    letters1 = []
                    for i in range(len(line)):
                        if line[i]!='-': letters1.append(line[i])
                    letters1_occ = Counter(letters1)
                    #letters1_occ = sorted(letters1_occ)
                    # letters = [letters[0][0],letters[0][1],letters[0][2],
                    #            letters[1][0],letters[1][1],letters[1][2],
                    #            letters[2][0],letters[2][1],letters[2][2]]
                    letters_occ = Counter(letters)
                    #letters_occ = sorted(letters_occ)
                    if letters1_occ - letters_occ == Counter():
                        if len(line)%2 != 0:
                            if line[len(line)//2] == letters[4]:
                                words.add(line)
                        else:
                            if (line[len(line)//2] == letters[4]
                            or line[len(line)//2-1] == letters[4]):
                                words.add(line)
    return words

get_words('en', 'jniarnoah')


def get_user_words() -> List[str]:
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish.
    """
    from sys import stdin
    u_words = []
    for line in stdin:
        u_words.append(line[:len(line) - 1])
    return u_words

def get_pure_user_words(user_words: List[str], letters: List[str], words_from_dict: List[str]) -> List[str]:
    """
    (list, list, list) -> list

    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    pass

def results():
    url = "en"
    letters = generate_grid()
    words_from_dict = get_words(url, letters)
    user_words = get_user_words()
    print(words_from_dict)
    print(user_words)
    get_pure_user_words(user_words, letters, words_from_dict)
    pass