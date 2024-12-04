"""This module contains utility functions for the Advent of Code 2024 puzzles."""

from os import getcwd


def load_data(day: int, test: bool = True):
    """Loads the puzzle data from file placed in data folder.

    Keyword arguments:
    day: int -- number of the day of the puzzle
    test: bool -- flag to load the test data (default is True) if set to False loads the puzzle data

    Return: return_description
    """
    with open(f"{getcwd()}/data/day{str(day)}{".test" if test else ""}.txt") as f:
        result = f.read().splitlines()
        return result


def grid(data: list[str]) -> list[list[str]]:
    """Converts a list of strings to a 2D grid.

    Keyword arguments:
    data: list[str] -- list of strings to convert to 2D grid

    Return: list[list[str]]
    """
    return [list(row) for row in data]
