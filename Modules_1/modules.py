############################## Modules ###################################
# A module is simply a file that contains Python code - functions, classes, and variables -
# Which you can import and reuse in other Python programs.
# Modules help you do the following:
# - Organize your code into seperate files
# - Reuse code across multiple programs
# - Keep your code easier to maintain and understand

# Modules are mapped to a file


################################### Creating Modules #########################################

# Don't use a * to import all of the functions from a module, only do the ones that are absolutely necessary. The reason for this
# is because you might have some functions or variables in a different module that can override what you have going on in your
# current file. To avoid anything bad from potentially happening, only import the functions that you need to accomplish the task

# States the module (or file) that you're importing from and which function from that module you're importing
import sys
from Modules_2.sales import calc_shipping, calc_tax
import Modules_2.sales
from Modules_2 import sales

# 2 ways to import a module above, either the entire module and use the . selector to select a specific method, or you can
# import each method seperately

# Calls the calc_shipping() and calc_tax() functions even though they're in a different file because they were imported

# The first example below comes from importing each function from the module seperately
calc_shipping()
calc_tax()

# The second option below comes from importing the module as a whole but selecting the desired function using the . selector
Modules_2.sales.calc_tax()
Modules_2.sales.calc_shipping()


#################################### Compiled Python Files ########################################
# When you run a function from a module in python a folder called _pycache_ will automatically be created.
# This folder is created for the module that you're importing. In the example with the current files structure that
# we have in place there was a file created for our sales module. If we imported more modules then we would have
# more files that were created. A _pycache_ file is only created for the file(s) that are being imported and not
# for the main file that the modules are being imported into. This file helps python run our program faster because
# the code from our module is being stored as compiled bytecode


##################################### Module Search Path ##########################################
# Above we imported the sales module. When we import the sales module python will look in the current directory for a sales.py
# file. If the file happens to not be there then there are some predefined places that python will also look to see if it can
# find the file.

# Above we imported the sys module. This will give us access to the path variable that we can use to see what paths Python
# will look at to see if it can find the file

print(sys.path)


####################################### Packages ##################################################
# Packages are mapped to a directory where modules are mapped to a file

# Packages are a way to store related modules together in a directory structure. In order for a folder to be considered a package
# we have to include a file called __init__.py in the folder so that python knows that the folder is now a package. However,
# when we use a package and we want to import a module, we'll have to prefix the name of the module with the name of the
# folder/package.

# For example. If we weren't using a package and we wanted to import the various functions from the sales module we would type
# sales.calc_tax() or sales.calc_shipping() if we were importing the entire module as a whole or calc_tax() and calc_shipping()
# if we'd already imported the functions at the top of the screen. If we implement the package system then calling these functions
# would turn into Modules_2.sales.calc_tax() and Modules_2.sales.calc_shipping(). However if we prefix the same of the package in
# the import statement then we won't have to worry about typing out the package name each time