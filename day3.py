"""Day: 3: Multiplication Madness"""

from utils import load_data
from re import findall


def execute(operation: str) -> int:
    """Executes the multiplication operation

    Keyword arguments:
    operation -- string representing the operation to execute
    Return: result of multiplication
    """
    x, y = operation[4:-1].split(",")
    return int(x) * int(y)


def filter_function(operations: list[str]) -> list[str]:
    """Filters the operations based on the don't() and do() operations

    Keyword arguments:
    operations -- list of operations to filter
    Return: list of filtered operations
    """
    result = []
    enabled = True

    for op in operations:
        if op == "don't()":
            enabled = False
        elif op == "do()":
            enabled = True

        if op.startswith("mul") and enabled:
            result.append(op)
    return result


data = "".join(load_data(3, False))
ops = findall(r"(mul\([0-9]{1,3},[0-9]{1,3}\))", data)
result = sum([execute(op) for op in ops])


ops2 = filter_function(findall(r"(mul\([0-9]{1,3},[0-9]{1,3}\)|don\'t\(\)|do\(\))", data))
result2 = sum([execute(op) for op in ops2])

print(f"Part 1: {result}")
print(f"Part 2: {result2}")
