from datetime import datetime, date

now = datetime.now()
print("Current date and time:", now)
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Hour:", now.hour)
print("Minute:", now.minute)

today = date.today()
print("\nToday's date:", today)

birthday = date(2005, 8, 15)
age_days = today - birthday
print("Days since Aditya's birthday:", age_days.days)

formatted = now.strftime("%d-%m-%Y %H:%M:%S")
print("Formatted:", formatted)
