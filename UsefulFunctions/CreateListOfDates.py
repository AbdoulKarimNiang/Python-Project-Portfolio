from datetime import datetime as dt
from datetime import timedelta
MIN_DATE = '2024-08-01'
MAX_DATE = '2024-11-30'

date_list = []

def create_list_date(min: str, max: str):

    min_date = dt.date(dt.strptime(min, '%Y-%m-%d' ))
    max_date = dt.date(dt.strptime(max, '%Y-%m-%d' ))

    difference = (max_date -  min_date).days

    date_list.append(min_date)

    new_date = min_date
    for i in range(difference):
        new_date += timedelta(days=1)
        date_list.append(new_date)

    return date_list
date_list = create_list_date(MIN_DATE, MAX_DATE)

# print(date)


for date in date_list:
    print(f"The correct date is {date}")
