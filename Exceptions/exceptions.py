########################## Handling Exceptions #############################

try:
    age = int(input("Age: "))
except ValueError as ex:
    print("You didn't enter a valid age")
    print(ex)
    print(type(ex))
else:
    print("No exceptions were thrown.")
print("Execution continues.")


######################## Handling Different Exceptions #########################

# try:
#     # with open("app.py") as file:
#     #     print("File opened.")
#     age = int(input("Age: "))
# except (ValueError, ZeroDivisionError):
#     print("You didn't enter a valid age.")
# else:
#     print("No exceptions were thrown.")


############################# Raising Exceptions ###########################

def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10 / age


calculate_xfactor(-1)
