################## CONTROL FLOW #####################

############### Comparison Operators ###############

print(10 > 3)  # Greater
print(10 >= 3)  # Greater or equal
print(10 < 20)  # Less then
print(10 <= 20)  # Less then or equal to
print(10 == 10)  # Comparison, not assignment
print(10 == "10")  # Comparison, not assignment
print(10 != "10")  # Not equal to
# Greater then. Since b comes after a this is true. The further down the alpahabet you get the larger the number
print("bag" > "apple")
# Comparison, not assignemnt. Not true, capital letters come first in the ord
print("bag" == "BAG")
print(ord("b"))  # Command to see where lower case b falls in the order listing
print(ord("B"))  # Command to see where capital B falls in the order listing


#################### Conditional Statements ##################
# If the if statement is executed then the other statements are skipped

temperature = 25  # Sets a variable called temperature equal to 15
if temperature > 30:  # If statement to see if the temperature is greater then 30
    # If the above statement is true then "It's warm" is printed
    print("It's warm")
    # If the above statement is true then "Drink water" is printed
    print("Drink water")
elif temperature > 20:  # elif statement which presents a different option. Checks to see if the temperature is greater then 20
    # If the above statement is correct then "It's nice" is printed
    print("It's nice")
# Assuming the if and elif statement(s) are false then the else statement will be executed
else:
    # If the else statement is executed then "It's cold" is printed
    print("It's cold")
print("Done")  # "Done" is printed regardless


################### Ternary Operator ###################

# if age >= 18:
#     message = "Eligible"
# else:
#     message = "Not Eligible"

age = 22  # Sets a variable called age equal to 22
# States that the variable of message is equal to "Eligible" if age is greater
message = "Eligible" if age >= 18 else "not Eligible"
# or equal to 18, otherwise the else statement is executed and "not Eligible" is printed on the screen

# Ternary Operators like the one above do the same thing as the if/else loop except the code is shorter

print(message)  # Prints the message on the screen


################# Logical Operators ####################

# and
# or
# not

# States that a variable called high_income is set to the boolean of True
high_income = True
# States that a variable called good_credit is set to the boolean of False
good_credit = False
student = True  # States that a variable called student is set to True

# and
if high_income and good_credit:  # States that both high_income and good_credit have to be true for "Eligible" to be printed
    print("Eligible")
else:  # If one or both of high_income or good_credit are false then "Not Eligible" is printed
    print("Not Eligible")

# or
if high_income or good_credit:  # Only high_income or good_credit have to be true for "Eligible" to be printed
    print("Eligible")
else:  # If both high_income and good_credit are false then "Not Eligible" is printed on the screen
    print("Not Eligible")

# not

if not student:  # States that if student is not True then "Eligible" is printed on the screen
    print("Eligible")
else:  # Otherwise, if student is True then "Not Eligible" will be printed
    print("Not Eligible")


# If either high_income or good_credit is True and student is False the "Eligible" is printed
if (high_income or good_credit) and not student:
    print("Eligible")
else:  # Otherwise, if both high_income and good_credit are both false then the statement is skipped, regardless if the student variable is false and "Not Eligible" is printed
    print("Not Eligible")


################ Short Circuit Evaluation ####################
# Logical Operators are short circut. If one of the variables in the expression turns out to be false and
# you're using the "and" operator then the entire expression will be evaluated to false, even if everything
# else is true. If you're using the "or" operator then even if one of the variables is false then the
# expression will continue to be evaluated because it assumes that there's still one that will be true. If one
# happens to be true then the enitre expression is evaluated to true, even though there's some that coule be false


################# Chaining Comparison Operators ###################

# age should be between 18 and 65

age1 = 66  # Sets a variable called age1 equal to 22
# if age1 >= 18 and age1 < 65: - Does the same thing as the line below
if 18 <= age1 < 65:  # Checks to see if age1 is greater then or equal to and age1 is less then 65
    print("Correct")  # If the above statement is true then "Correct" is printed
else:  # If age1 is 17 or less or 65 or greater then "Not Correct" will be printed
    print("Not Correct")


################### For Loops ####################

# Start at the #1 but end before #4, 4 is not included in the loop, it's everything up until 4
for number in range(1, 10, 2):  # You can also include a third argument that is a step (1, 10, 2) would say start at 1, go to 10 but incrament by 2 each iteration
    print("Attempt", number, number * ".")


################# For Else ######################

successful = False  # Sets a variable called successful equal to False
# Sets a variable called number1 for each loop iteration. Range(3) states that it's going to be run 3 times
for number1 in range(3):
    # For each iteration the word "Attempt" is printed in the terminal
    print("Attempt")
    if successful:  # If successful is true then the word "Successful" is printed and the break statement breaks and leaves the loop
        print("Successful")
        break
else:  # If after the 3 iterations and successful is still false then the following statement is printed in the terminal
    print("Attempted 3 times and failed")


################# Nested Loops #######################

for x in range(5):  # The iteration starts out with 0
    for y in range(3):  # The iteration starts out with 0
        # With each iteration the coordinates will be printed
        print(f"({x}, {y})")


#################### Iterables ######################
# Iterable objects:
# - Range
# - String
# - List

# Iterable simply means that we're able to execute over it in a loop. With each iteration the variable will have a different value

print(type(5))  # Prints out the type of 5
print(type(range(5)))  # Prints out the typs of range(5)

for x in range(4):  # Defines a variable called x and will reassign it's value for each number in the range
    print(x + 1)  # Prints out each number on a seperate line

for x in "Python":  # Defines a variable called x and will reassign it's value for each character in the word "Python"
    print(x)  # Prints out each letter of the word on a seperate line

for x in [1, 2, 3, 4]:  # Defines a variables called x and will reassign it's value for each letter in the list
    print(x)  # Prints out each number on a seperate line


################# While Loop ###################
# The loop will continue as long as then condition is still true
# Use a break statement to avoid getting stuck in an infinit loop

number2 = 100  # Defines a variable called number2 equal to 100

while number2 > 0:  # States that while the number2 is greater then 0 continue the loop
    print(number2)  # Prints number2 after each loop iteration
    number2 //= 2  # Divides the number2 in half with each iteration


command = ""  # Sets a variable called command equal to an empty string
# while command.lower() != "quit":  # States that while command does not equal "quit", continue *Note* - the program is converting the command variable to lower case
# so that it doesn't matter how the user enters the word quit it will convert it all to lower case and check to see if it matches before quiting the loop
# command = input(">")  # Gets user input in the terminal
# print("ECHO", command)  # Prints out what the users typed into the terminal

################# Exercise ######################

count = 0
for number in range(1, 10):
    if number % 2 == 0:
        count += 1
        print(number)
print(f"We have {count} even numbers")
