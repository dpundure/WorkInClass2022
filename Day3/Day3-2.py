salary = int(input("How much do you earn monthly? "))
years = float(input("How many years have you worked in our company? "))
if years >= 2:
    bonus = 0.15 * salary * (years -2)
    print(years,"years of experience,",salary," Euro salary, the bonus will be",bonus,"Euro")
else:
    print(years,"years of experience,",salary," Euro salary, no bonus (0)")

