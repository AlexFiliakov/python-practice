def is_leap_year(year):
    """Determine if year is a leap year.

    Arguments:
        year -- integer year
    """
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False
