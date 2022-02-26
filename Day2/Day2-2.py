width = float(input("What is rooms width in meters? "))
lenght = float(input("What is rooms lenght in meters? "))
height = float(input("What is rooms height in meters? "))
volume = width * lenght * height
rounded_volume = round(volume,2)
print("Volume of the room in is cubicmeters",rounded_volume)