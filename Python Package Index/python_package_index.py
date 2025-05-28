##################################### Python Package Index #####################################

####################### Pypi ####################
# When using python there might be somethings that are not in the python library by default. By going to
# pypi.org we can find other packages that are developed by python users that we can use in our programs

###################### Pip ##########################
# Pip is used to install and uninstall packages in python

############################## Virtual Environments #################################
# When we simply download the latest version of a package we are restricting ourselves. If we're working
# on a project and we want to use an older version of a particular package we can't do that because we
# can't have two different versions of the same package running side by side. To solve this we create
# an isolated virtual environment and install the different packages to the virtual environment

##################################### Pipenv ########################################
# Pipenv combines pip and virtual environments into one tool chain

################################# Virtual Environments in VSCode #################################
# Virtual environments in VSCode allow you to run a variety of packages that are in different files
# on your computer

###################################### Pipfile ###############################################
# The pipfile holds all of the differnt dependencies of our application so that a virtual environment
# can be duplicated on different machines in order to run the program

###################################### Managing Dependencies ######################################
# pipenv graph -> shows all of the installed dependencies
# pipenv update --outdated -> shows outdated packages
# pipenv update -> updates all of the packages
# pipenv update {package_name} -> Only updates a spcific package


####################################### Publishing Packages ###########################################
# To upload your own package to pypi.org you first have to create an account and activate it. After the
# account is activated you will need to install 3 tools:
# pip install setuptools wheel twine

######################################### Docstrings ###########################################
# When we create a package that goes into pypi.org we need to document the code so that users that are going
# to be using it are able to understand better what the code is doing. This can be done by surrounding the
# instruction with triple """

########################################## Pydoc #####################################################
# To view the documentation for a module run the following command: pydoc {module_name}