import datetime
from datetime import date

Birth = input("Please Enter your Birth date as(%d-%m-%y): ")
try:
    day, month, year = map(int, Birth.split('-'))
except:
    day, month, year = map(int, Birth.split('/'))

Today = date.today()
Birth = datetime.date(year, month, day)

NOD = Today - Birth

print(f"Congratulations! You have completed {NOD.days} days in your Lifetime")
print(f"You are {int(NOD.days / 365)} years old.")
