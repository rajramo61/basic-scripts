def days_between_dates(year1, month1, day1, year2, month2, day2):
    """
    Calculates the number of days between two dates.
    """
    month_days_mapper = {1: 0, 2: 31, 3: 59, 4: 90, 5: 120, 6: 151, 7: 181, 8: 212, 9: 243, 10: 273, 11: 304, 12: 334}
    leap_year_month_days_mapper = {1: 0, 2: 31, 3: 60, 4: 91, 5: 121, 6: 152, 7: 181, 8: 213, 9: 244, 10: 274, 11: 305,
                                   12: 335}
    # TODO - by the end of this lesson you will have
    #  completed this function. You do not need to complete
    #  it yet though!
    total_days = 0
    total_days = calculate_days_without_leap_year(day1, day2, month1, month2, month_days_mapper, year1, year2)
    total_leap_years = find_all_leap_years_additional_days(year1, month1, day1, year2, month2, day2)
    total_days += total_leap_years
    return total_days


def find_all_leap_years_additional_days(year1, month1, day1, year2, month2, day2):
    """
    :param year1:
    :param month1:
    :param day1:
    :param year2:
    :param month2:
    :param day2:
    :return:
    """
    total_leap_years = 0
    if is_leap_year(year1) and month1 < 3:
        total_leap_years += 1
    for year in range(year1 + 1, year2):
        if is_leap_year(year1):
            total_leap_years += 1
    if is_leap_year(year2) and month2 > 1 and day2 > 28:
        total_leap_years += 1
    return total_leap_years


def is_leap_year(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def is_leap_year_class(year):
    if (year % 400) == 0:
        return True
    if (year % 100) == 0:
        return False
    if (year % 4) == 0:
        return True


def calculate_days_without_leap_year(day1, day2, month1, month2, month_days_mapper, year1, year2):
    if year1 == year2:
        if month1 == month2:
            return day2 - day1
        total_days = month_days_mapper.get(month2) - month_days_mapper.get(month1)
        return calculate_days(day1, day2, total_days)
    else:
        total_days = (year2 - year1) * 365
        if month2 > month1:
            total_days += (month_days_mapper.get(month2) - month_days_mapper.get(month1))
            return calculate_days(day1, day2, total_days)
        else:
            total_days -= (month_days_mapper.get(month1) - month_days_mapper.get(month2))
            return calculate_days(day1, day2, total_days)


def calculate_days(day1, day2, total_days):
    if day2 > day1:
        total_days += (day2 - day1)
        return total_days
    else:
        total_days -= (day1 - day2)
        return total_days


def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def test_days_between_dates():
    # test same day
    assert (days_between_dates(2017, 12, 30,
                               2017, 12, 30) == 0)
    # test adjacent days
    assert (days_between_dates(2017, 12, 30,
                               2017, 12, 31) == 1)
    # test new year
    assert (days_between_dates(2017, 12, 30,
                               2018, 1, 1) == 2)
    # test full year difference
    assert (days_between_dates(2012, 6, 29,
                               2013, 6, 29) == 365)

    assert (is_leap_year(2012) == True)

    assert (find_all_leap_years_additional_days(2012, 1, 1,
                                                2013, 1, 1) == 1)
    assert (days_between_dates(2012, 1, 1,
                               2013, 1, 1) == 366)

    print("Congratulations! Your daysBetweenDates")
    print("function is working correctly!")


test_days_between_dates()
