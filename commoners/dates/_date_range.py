from datetime import date, timedelta
from typing import Generator


def convert_to_first_day_of_month(d: date) -> date:
    """
    Convert a date to the first day of its month.

    Args:
        d (date): The input date.

    Returns:
        date: The first day of the month.
    """
    return date(d.year, d.month, 1)


def convert_to_last_day_of_month(d: date) -> date:
    """
    Convert a date to the last day of its month.

    Args:
        d (date): The input date.

    Returns:
        date: The last day of the month.
    """
    if d.month == 12:
        return date(d.year, d.month, 31)
    else:
        next_month = date(d.year, d.month + 1, 1)
        last_day = next_month - timedelta(days=1)
        return last_day


def months_between(start: date, end: date) -> Generator[date, None, None]:
    """
    Generate a list of months between start and end (inclusive).

    Args:
        start (date): The start date.
        end (date): The end date.
    Yields:
        a list of months between start and end (inclusive).
    """

    current_date = date(start.year, start.month, 1)
    end_ = date(end.year, end.month, 1)
    while current_date <= end_:
        yield current_date

        if current_date.month != 12:
            current_date = date(current_date.year, current_date.month + 1, 1)            
        else:
            current_date = date(current_date.year + 1, 1, 1)


def dates_between(start: date, end: date) -> Generator[date, None, None]:
    """
    Generate a list of dates between start and end (inclusive).

    Args:
        start (date): The start date.
        end (date): The end date.

    Yields:    
        a list of dates between start and end (inclusive).
    """
    current_date = start
    while current_date <= end:
        yield current_date
        current_date += timedelta(days=1)
