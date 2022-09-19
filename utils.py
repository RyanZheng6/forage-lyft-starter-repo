def add_years_to_date(original_date, years_add):
    output = original_date.replace(year=original_date.year + years_add)
    return output