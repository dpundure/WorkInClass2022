users_temperature = float(input("What is your temperature? "))
if users_temperature < 35:
    print("not too cold")
elif users_temperature > 37:
    print("possible fever")
else:
    print("all right")

