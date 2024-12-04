"""Day 4: Checking for XMASS words
"""

from utils import load_data, grid
from numpy import rot90


def slant(page: list[list[str]], step: int = 1) -> list[list[str]]:
    """Returns the slant of the page

    Keyword arguments:
    page -- list of strings to slant
    offset -- offset of the slant (default is 1) if set to -1 returns the anti-slant
    Return: slanted page
    """
    slanted = []
    for i in range(len(page)):
        lpad = i if step > 0 else len(page) - 1 - i
        rpad = len(page) - 1 - i if step > 0 else i
        slanted.append(["."] * lpad + page[i] + ["."] * rpad)
    return slanted


def count_word(page: list[list[str]], word: str) -> int:
    """Finds the specified words in the page

    Keyword arguments:
    page -- list of strings to search for the word
    word -- word to search for
    Return: a number of occurrences of the word
    """
    result = 0
    rword = word[::-1]
    pages = []
    pages.extend(page)
    pages.extend(rot90(page))
    pages.extend(rot90(slant(page)))
    pages.extend(rot90(slant(page, -1)))
    for row in pages:
        result += "".join(row).count(word)
        result += "".join(row).count(rword)
    return result


def count_x(page: list[list[str]]) -> int:
    """Finds MAS in the shape of an X on the page

    Keyword arguments:
    page -- the page provided by elf split into a grid
    Return: a number of occurences of the X shaped MAS
    """

    result = 0
    for row in range(1, len(page) - 1):
        for col in range(1, len(page[row]) - 1):
            if page[row][col] == "A" and (
                (page[row - 1][col - 1] == "M" and page[row + 1][col + 1] == "S") or (
                    page[row - 1][col - 1] == "S" and page[row + 1][col + 1] == "M")
            ) and (
                (page[row - 1][col + 1] == "M" and page[row + 1][col - 1] == "S") or (
                    page[row - 1][col + 1] == "S" and page[row + 1][col - 1] == "M")
            ):
                result += 1
    return result


grid = grid(load_data(4, False))
print(f"Part 1: {count_word(grid, "XMAS")}")
print(f"Part 2: {count_x(grid)}")
