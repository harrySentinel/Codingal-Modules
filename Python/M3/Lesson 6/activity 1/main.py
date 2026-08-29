import datetime
import calendar

student_name = "Aditya Srivastava"
today = datetime.date.today()
print("Hey", student_name, "! Today's date is", today)
print("Day of the week:", calendar.day_name[today.weekday()])

now = datetime.datetime.now()
print("Current time is", now.strftime("%H:%M:%S"))

birth_year = int(input("Enter your birth year: "))
age = today.year - birth_year
print("You will turn", age, "this year")

print("\nHere is the calendar for this month")
print(calendar.month(today.year, today.month))
