from datetime import date


def get_term():
    today = date.today()
    last_day = date(day=28, month=11, year=2022)
    term = last_day - today
    term = term.days
    if term == 1:
        term = f'{term} день'
    elif term > 1 and term <= 4:
        term = f'{term} дня'
    elif term >= 4:
        term = f'{term} дней'
    else:
        term = None
    return term
