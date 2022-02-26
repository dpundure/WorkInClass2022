import datetime

my_surname = input("What is your surname? ")
my_age = int(input(f"How old are you,{my_surname}? "))
left_years = 100 - my_age
print(left_years,"years left to be 100 years old")
current_Year = datetime.datetime.now().year
year = current_Year + left_years
print(f"On year {year} you will be 100 years old.")