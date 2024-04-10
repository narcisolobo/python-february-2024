from datetime import date
from dateutil.relativedelta import relativedelta
from inflect import engine


def age(birthday):
    inflect = engine()
    today = date.today()
    years = relativedelta(today, birthday).years
    months = relativedelta(today, birthday).months
    if years < 1:
        return f"{inflect.number_to_words(months)}-month-old"
    return f"{inflect.number_to_words(years)}-year-old"
