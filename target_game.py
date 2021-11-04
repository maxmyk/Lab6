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
    filea = open(file, "w", encoding='utf-8')
    for line in filea:
        line = line.lower()
        line = line.strip()

    pass



def get_user_words() -> List[str]:
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish.
    """
    u_words = []
    for line in input():
        u_words.append(line[:len(line) - 1])
    return u_words
    pass


def get_pure_user_words(user_words: List[str], letters: List[str], words_from_dict: List[str]) -> List[str]:
    """
    (list, list, list) -> list

    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    pass


def results():
    pass
