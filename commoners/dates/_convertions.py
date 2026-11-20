from datetime import date, timedelta


from commoners.models import Period


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


def split_month_in_half(d: date) -> tuple[Period, Period]:
    y, m = d.year, d.month

    first_period = Period(
        start=date(y, m, 1),
        end=date(y, m, 14)
    )
    second_period = Period(
            start=date(y, m, 15),
            end=convert_to_last_day_of_month(d)
    )

    return first_period, second_period


def split_month_in_quarters(d: date):
    y, m = d.year, d.month

    first_period = Period(
        start=date(y, m, 1),
        end=date(y, m, 7)
    )
    second_period = Period(
        start=date(y, m, 8),
        end=date(y, m, 15),
    )
    third_period = Period(
        start=date(y, m, 16),
        end=date(y, m, 23),
    )
    fourth_period = Period(
        start=date(y, m, 24),
        end=convert_to_last_day_of_month(d)
    )

    return first_period, second_period, third_period, fourth_period
