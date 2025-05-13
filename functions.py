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

def get_greeting(name):
    return f"Hi {name}"


message = get_greeting("Brantley")
file = open("content.txt", "w")
file.write(message)


#################### Keyword Arguments #####################

def increment(number, by):
    return number + by


print(increment(number=2, by=1))


#################### Default Arguments #####################

def increment1(number, by=1):  # Optional parameters come after all of the required parameters
    return number + by


print(increment(2, 5))


##################### Xargs ##########################

def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3, 4, 5))


#################### Xxargs #######################
# When we use a double astrigs (**) as a parameter it allows us to pass in multiple key, value pairs to the function. These key,value
# pairs are going to be stored in a dictionary to be access later

def save_user(**user):
    print(user)
    # print(user["id"]) will print the value of the "id" key
    # print(user["name"]) will print the value of the "name" key
    # print(user["age"]) will print the value of the "age" key


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

def multiply1(*numbers):
    total1 = 1
    for number in numbers:
        total1 *= number
    return total1


print("Start")
print(multiply1(1, 2, 3))


#################### Exercise ######################
# Input divisible by 3 -> Fizz
# Input divisible by 5 -> Buzz
# Input divisible by 3 & 5 -> Fizz Buzz
# Input not divisible by 3 or 5 -> Return the input

def fizz_buzz(input):
    if (input % 5 == 0) and (input % 3 == 0):
        return "FizzBuzz"
    elif input % 3 == 0:
        return "Fizz"
    elif input % 5 == 0:
        return "Buzz"
    else:
        return input


print(fizz_buzz(3))
