height = int(input("Enter tree height: "))

for i in range(height):
    a = height - i + 1
    print(" " * a, end="")
    print("*"*(i*2+1))
