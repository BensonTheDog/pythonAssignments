"""

Jerame Kim 2/7/2019
Program name:  assignment_5

Part 1
Taking user input and outputting a string telling them whether or not
it is a prime number

Part 2
Making a function that takes user input and outputs a string telling
them whether or not it is a prime number

Part 3
Taking the function from Part 2 and inserting it in a loop to find
the first 3 prime number greater than 1000

"""

# Part 1

# Take user input, parse it into a integer and assign it to
# variable named number
number = int(input("Enter a number: "))

# x is the divisor, and increments from 2 to the number
# given to the function
for x in range(2, number):
    # if the remainder from input divided by x is equivalent to 0
    # #this is not a prime number
    if (number % x) == 0:
        # if the number is not a prime number, print the number and string
        # that states it is not a prime number
        print(number, "is not a prime number")
        break
# if none of quotients are zero, it is a prime number
# print the number and string that states it is not a prime number
else:
    print(number, "is a prime number")


# Part 2

# Make the above loop into a function with manual input "number"
def isPrime(number):
    # x is the divisor, and increments from 2 to the number
    # given to the function
    for x in range(2, number):
        # if the remainder from input divided by x is equivalent to 0
        # this is not a prime number
        # return 0 if it is not a prime number
        if (number % x) == 0:
            return 0
            break
    # if none of quotients are zero, it is a prime number
    # return the input
    else:
        return number


# Part 3

# Initialize the counter used to stop the loop when
# 3 primes numbers are output
counter = 0

# Set a for loop with the provided range
for x in range(1000, 1500):
    # Run the function made in part 2
    isPrime(x)

    # If the counter is not equal to three this runs
    if counter != 3:
        # when the output from isPrime() returns any number but zero
        # and it is prime, it prints the number
        # and it also increments the counter
        if isPrime(x) != 0:
            print(isPrime(x))
            counter += 1
    # because the counter starts at 0,
    # when it reaches 3 it skips the if statement and ends the loop
    else:
        break

"""
[PART 1 OUTPUT]
-------------------------- run ------------------------- 
/Users/jerame/Development/pythonAssignments/Assignment_5/venv/lib/main.py
Enter a number: 3
3 is a prime number

Process finished with exit code 0

-----------------------end of run-----------------------

[PART 2/3 OUTPUT]
-------------------------- run ------------------------- 
/Users/jerame/Development/pythonAssignments/Assignment_5/venv/lib/main.py
1009
1013
1019

Process finished with exit code 0


-----------------------end of run-----------------------
"""