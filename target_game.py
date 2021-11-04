"""
Target game
"""

from typing import List
"""
Importing Lists
"""


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
    grid.pop()
    print(grid)
    return grid


def get_words(file: str, letters: List[str]) -> List[str]:
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    """
    from collections import Counter
    words = set()
    with open(file, "r", encoding='utf-8') as file:
        for line in file:
            line = line.lower()
            line = line.strip()

            if len(line) >= 4 and letters[4] in line:
                letters1 = []
                for i in range(len(line)):
                    if line[i] != '-':
                        letters1.append(line[i])
                letters1_occ = Counter(letters1)
                letters_occ = Counter(letters)
                if letters1_occ - letters_occ == Counter():
                    words.add(line)
    return sorted(list(words))


def get_user_words() -> List[str]:
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish.
    """
    from sys import stdin
    u_words = set()
    for line in stdin:
        u_words.add(line[:-1])
    return sorted(u_words)


def get_pure_user_words(user_words: List[str
], letters: List[str], words_from_dict: List[str]) -> List[str]:
    """
    (list, list, list) -> list

    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    words = set()
    wfd = set(words_from_dict)
    from collections import Counter
    for word in user_words:
        if len(word) >= 4 and letters[4] in word and word not in wfd:
            letters1 = []
            for i in range(len(word)):
                if word[i] != '-':
                    letters1.append(word[i])
            letters1_occ = Counter(letters1)
            letters_occ = Counter(letters)
            if letters1_occ - letters_occ == Counter():
                words.add(word)
    return sorted(list(words))


def results():
    """
    Prints results
    """
    letters = generate_grid()
    letters = [letters[0][0], letters[0][1], letters[0][2],
               letters[1][0], letters[1][1], letters[1][2],
               letters[2][0], letters[2][1], letters[2][2]]
    words_from_dict = get_words('en', letters)
    user_words = get_user_words()
    filea = open("result.txt", "w", encoding='utf-8')
    for line in get_pure_user_words(user_words, letters, words_from_dict):
        filea.write(line+'\n')
    filea.close()
