from datetime import date, timedelta

today = date.today()

dates_between = [
    today + timedelta(days=i)
    for i in range(7)
]

dates = []

for d in dates_between:
    dates.append(d.strftime('%d-%m-%Y'))
