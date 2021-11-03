"""
Sorts songs
"""
from typing import List, Tuple, Callable, Union
"""
importing List, Tuple, Callable, Union
"""


def song_length(tup: Tuple[str]) -> float:
    """
    Returns: lengths of songs
    >>> song_length(('Янанебібув', '3.19'))
    3.19
    """
    try:
        return float(tup[1])
    except ValueError:
        pass


def title_length(tup: Tuple[str]) -> int:
    """
    Returns: lengths of songs
    >>> title_length(('Янанебібув', '3.19'))
    10
    """
    try:
        return len(tup[0])
    except ValueError:
        pass


def last_word(tup: Tuple[str]) -> str:
    """
    Returns: lengths of songs
    >>> last_word(('Янанебібув', '3.19'))
    'Я'
    """
    try:
        return tup[0].split()[-1][0]
    except ValueError:
        pass


def sort_songs(
        song_titles: List[str],
        length_songs: List[str],
        key: Callable[[tuple], Union[int, str, float]]) -> List[tuple]:
    """
    Returns sorted list of songs
    >>> sort_songs(['Янанебібув', 'Той день'], ['3.19', '3.58'], song_length)
    [('Янанебібув', '3.19'), ('Той день', '3.58')]
    """
    if len(song_titles) == len(length_songs):
        if type(song_titles) == list and type(length_songs) == list:
            tup = tuple((song_titles[i], length_songs[i])
                        for i in range(len(length_songs)))
            return sorted(tup, key=key)


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
