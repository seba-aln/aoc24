""" Day2: Report analysis
"""
from utils import load_data

data = [row.split() for row in load_data(2, False)]
reports, reports_dampened = [], []


def validate(report: list[int]) -> bool:
    """Check if the report levels are okay

    Keyword arguments:
    report -- list of integers representing the report levels
    Return: True if the report is valid, False otherwise
    """

    return all([0 < abs(diff) <= 3 for diff in report]) and (
        all([diff < 0 for diff in report]) or all([diff > 0 for diff in report])
    )


def problem_dampener(row: list[str]) -> list[int] | None:
    """Dampens the problem by removing one element from the report

    Keyword arguments:
    row -- list of strings representing the report
    Return: list of integers representing the dampened report
    """
    for i in range(len(row)):
        candidate = row[:i] + row[i + 1:]
        report = [int(candidate[i + 1]) - int(candidate[i]) for i in range(len(candidate) - 1)]
        if validate(report):
            return report
    return None


for row in data:
    report = [int(row[i + 1]) - int(row[i]) for i in range(len(row) - 1)]
    valid = validate(report)
    if valid:
        reports.append(report)
        reports_dampened.append(report)
    else:
        dampened = problem_dampener(row)
        print(f'Report dampener: {dampened}')
        if dampened:
            reports_dampened.append(dampened)

print(f"Part 1: {len(reports)}")

print(f"Part 2: {len(reports_dampened)}")
