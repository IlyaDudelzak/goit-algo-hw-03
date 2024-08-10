from datetime import datetime, date, timedelta

def string_to_date(date_string):
  return datetime.strptime(date_string, "%Y-%m-%d").date()

def get_days_from_today(date_):
  try:
    today = date.today()
    delta = today - string_to_date(date_)
    return delta.days
  except ValueError:
    print("Wrong date format!")
    return 0

print(get_days_from_today("2021-03-05"))