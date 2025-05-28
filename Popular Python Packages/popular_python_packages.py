 ########################### Popular Python Packages ###################################

############################# What are APIs ###########################################
# APIs are a way for a website to make their data available to others. They are endpoints
# that can be accessed on the internet through a URL

# The example below is building an application using the Yelp API

# If we're going to sent HTTP requests then we will need to import the requests module at
# the top of our page and make sure that we install requests, using pipenv. Typically we
# will need to get the request and store it in a variable similar to what's below

# url = {URL}
# api_key = {API Key}
# headers = {
# "Authorization": "Bearer " + api_key
# }
# params = {
#   "term": "Barber"
#   "location": "NYC"
# }
# response = requests.get({URL}, headers=headers, params)
# businesses = response.json()["businesses"]
# print(businesses)
# for business in businesses:
#   print(business["name"])

# names = [business["name"] for business in businesses if business["rating"] > 4.5]
# print(names)


################################## Hiding API Keys ####################################
# When we're building an application and we have an API key we want to make sure that we don't
# include the API Key in the source code. The reason being if we're going to be pushing our
# code to Github or some public repository we don't want that API Key to be in the hands of
# others because we would get in trouble if that API key was used in a bad way. The way that we
# fix this is we crate a new file and call it something such as config.py. We would then put a
# variable in this new config file to store the API key. We will then import that into the file
# that has all of the source code. Now, we want to make sure that that file doesn't get committed
# to GitHub so we want to create a .gitignore file at the root of our directory and put the name
# of that config file in the .gitignore file so that when we push code to Github the file that
# has our API key is not included in the code push