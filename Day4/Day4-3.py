# Primes
# Check if entered positive number is a prime number.
# A prime number is a number that divides without remainder only by itself and 1.
# Hint: what numbers do we have to check?

number = int(input("Enter a positive number: "))
is_prime_number = True
if number > 1:
    for i in range(2, number):
        if number % i == 0:
            is_prime_number = False
            print("Number is not a prime number")
            break
    else:
            print("Number is a prime number")






