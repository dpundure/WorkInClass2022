numbers_list = []

while True:
    numbers = input("Enter some number or 'q' to exit: ")
    if numbers == 'q':
        break
    else:
        numbers_list.append(float(numbers))
        average_number = sum(numbers_list)/len(numbers_list)
        print("Average number of all entered values", numbers_list, "is:", average_number) # prints all numbers and average
        print("TOP3 numbers you entered are:", sorted(numbers_list)[-3:],
              "and average number of all entered numbers is:", average_number) # prints top3 and average
        print("BOTTOM3 numbers you entered are:", sorted(numbers_list)[:3],
              "and average number of all entered numbers is:", average_number) # prints bottom3 and average
