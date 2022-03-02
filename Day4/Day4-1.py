start = 1
end_number = 100
fizz = 5
buzz = 7

for i in range(start, end_number + 1):
    if i % (fizz * buzz) == 0:
        print("FizzBuzz,", end=",")
    elif i % fizz == 0:
        print("Fizz", end=",")
    elif i % buzz == 0:
        print("Buzz", end=",")
    else:
        print(i, end=",")
