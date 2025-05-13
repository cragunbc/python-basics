######################## FUNCTIONS #########################
# Make sure that functions have meaningful names, are lower case, and have an underscore to seperate words instead of a space


################## Defining Functions ###################

def greet():  # Defines a new function called greet that takes no parameters
    # Prints the words "Hi there" as part of the function being called
    print("Hi there")
    # Prints the words "Welcome aboard" as part of the function being called
    print("Welcome aboard")


greet()  # Calls the greet function


################# Arguments ####################
# If our function has two parameters then we're required to pass in two arguments when calling the function

def name(first_name, last_name):  # Defines a new function called name that takes two parameters called first_name and last_name
    # Prints out the first_name and last_name in the terminial
    print(f"Hi {first_name} {last_name}")
    print("Welcome aboard")  # Prints out the words "Welcome aboard"


# Calls the function and passes in the two parameters for first_name and last_name
name("Brantley", "Cragun")
name("John", "Smith")


##################### Types of Functions #######################
# 1- Perform a task
# 2- Return a value

def get_greeting(name):  # Defines a function called get_greeting and requires the parameter of name
    # Returns the statement "Hi {name}", using the parameter that was provided
    return f"Hi {name}"


# Sets a variable called message and sets it equal to the value that is passed
message = get_greeting("Brantley")
# back from the get_greeting function with the argument that we're passing in. Result -> "Hi Brantley"
# This line of code will either open or create a new file called "content.txt"
file = open("content.txt", "w")
# in write mode, hense the "w"
# Writes the content of what was executed from the function into the file that was opened
file.write(message)
file.close()  # Closes the file


#################### Keyword Arguments #####################

def increment(number, by):  # Defines a function called increment and requires the two parameters of number and by
    return number + by  # Returns the value of number + by


# Prints in the terminal the result of calling the increment function and passing
print(increment(number=2, by=1))
# in the arguments of number=2 and by=1 which would give us 3


#################### Default Arguments #####################
# A default argument is an argument that is used if there isn't one that is provided from the user

def increment1(number, by=1):  # Optional parameters come after all of the required parameters
    return number + by  # Returns the value of number + by


# Gives us the result of 7 because we provided values for both arguments, so the default argument wasn't used
print(increment(2, 5))
# Gives us the result of 3 because we only provided the required argument and not the second argument in
print(increment1(2))
# addition so the default arugment is used to fullfill the need


##################### Xargs ##########################
# Allows you to pass through any number of arguments to the function and it will accept all of them

def multiply(*numbers):  # Defines a function called multiply and allows any number of numbers to be passed through as the parameter
    total = 1  # Defines a variable called total and sets it to 1
    for number in numbers:  # Starts a for loop that will loop over each number that's in the numbers list that's passed as the parameter
        total *= number  # For each number it is multiplied by the total and the total is then set to the new current value
    return total  # Once all of the numbers have been executed then the total value of all the numbers is returned


print(multiply(2, 3, 4, 5))  # Prints out the result


#################### Xxargs #######################
# When we use a double astrigs (**) as a parameter it allows us to pass in multiple key, value pairs to the function. These key,value
# pairs are going to be stored in a dictionary to be access later

def save_user(**user):  # Defines a function called save_user and requires the parameter of user
    # Prints the user is a structured format that has all of the key/value pairs
    print(user)
    print(user["id"])  # Prints the value of the "id" key
    print(user["name"])  # Prints the value of the "name" key
    print(user["age"])  # Prints the value of the "age" key


# Calls the save_user function and passes in 3 key/value pairs
save_user(id=1, name="Brantley", age=25)


#################### Scope ######################
# Scope talks about where you're pulling values from. Global scoped variables aren't good because they can cause problems down the road
# Always try to stick to local variables so that everything stays more clean and avoids confusion

message1 = "a"  # Global Variable


def greet1(name):
    message1 = "b"  # Local Variable


# Calls the greet1 function and passes in "Brantley" as the argument
greet1("Brantley")
print(message1)  # Prints the global message1 variable and not the one in the function because you can't call a variable in a function
# from outside the function


################### Debugging ######################

def multiply1(*numbers):  # Creates a function called multiply1 and requires some amount of numbers through the numbers parameter
    total1 = 1  # Defines a variable called total1 and sets it equal to 1
    for number in numbers:  # Loops through each number in the list of numbers that come from the parameter
        total1 *= number  # For each number the total1 is multiplied by that number
    return total1  # After all of the numbers have been executed the new total is returned to the user


print("Start")  # Prints the word "Start" in the terminal
# Prints the result of calling the multiply1 function and passing in a list of numbers
print(multiply1(1, 2, 3))


#################### Exercise ######################
# Input divisible by 3 -> Fizz
# Input divisible by 5 -> Buzz
# Input divisible by 3 & 5 -> Fizz Buzz
# Input not divisible by 3 or 5 -> Return the input

def fizz_buzz(input):  # Defines a function called fizz_buzz and requires a parameter called input
    # if statement to say that if the remainder of the the input divided by 5
    if (input % 5 == 0) and (input % 3 == 0):
        # is equal to 0 and the remainder of the input divided by 3 is equal to 0 the "FizzBuzz" is printed in the terminal
        return "FizzBuzz"
    elif input % 3 == 0:  # elif statement that says if the remainder of the input divided by 3 is equal to 0 then "Fizz"
        # is printed in the terminal
        return "Fizz"
    elif input % 5 == 0:  # elif statement that says if the remainder of the input divided by 5 is equal to 0 then "Buzz"
        # is printed in the terminal
        return "Buzz"
    else: # else statement that says that if none of the above conditions are met then the users original input is printed 
        # in the terminal
        return input


print(fizz_buzz(15)) # Prints the result of calling the fizz_buzz function
