def string_to_date(date_string):
  return datetime.strptime(date_string, "%Y-%m-%d").date()

def get_days_from_today(date_):

  today = date.today()
  delta = today - string_to_date(date_)
  return delta.days
