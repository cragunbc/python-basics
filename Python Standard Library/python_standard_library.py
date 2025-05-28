###################################### Python Standard Library #################################################

from pathlib import Path
from time import ctime
import shutil
from zipfile import ZipFile
import csv
import json
import sqlite3
import time
from datetime import datetime, timedelta
import random
import string
import webbrowser
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
import smtplib
from string import Template
import sys
import subprocess

#################################### Working With Paths ################################################
# Normally we'd need 2 backslashes, but with the "r" at the front we're using what's called a raw string. With a
# raw string escape characters such as a backslash aren't treated as an escape character

# Creates a variable called path1 and stores the relative path to the __init__.py file
path1 = Path("ecommerce/__init__.py")
path1.exists()  # Checks to see if the file/directory exists or not
path1.is_file()  # Checks to see if the path represents a file
path1.is_dir()  # Checks to see if the path represents a directory
print(path1.name)  # Prints the name of the file, i.e. __init__.py
print(path1.stem)  # Prints out the file name without the extension
print(path1.suffix)  # Prints out the extension of the file
print(path1.parent)  # Prints out the parent directory of the file
# Creates a new path object, based off of the current path but only changing the name
path2 = path1.with_name("file.txt")
# Prints the current path object but represents it using a different extension
path3 = path1.with_suffix(".txt")
print(path3)
print(path2.absolute())  # Prints out the absolute path of the object


#################################### Working with Directories ########################################

path4 = Path("ecommerce")
# path4.exists() - Checks to see if a directory exists
# path4.mkdir() - Creates a new directory
# path4.rmdir() - Removes a directory
# path4.rename("ecommerce2") - Changes the name of the directory
# print(path4.iterdir()) - Returns the list of files and directories in the particular path


################################## Working with Files ################################################
path5 = Path("ecommerce/__init__.py")
# path5.exists() # Checks to see if the files exists
# path5.rename("init.txt") # Renames the file
# path5.unlink() # Deletes the file
# path5.stat() # Returns various stats on on the file
# print(ctime(path.stat().st_ctime)) - Prints out a viewable version of the time from the code line above
# print(path5.read_text())
# path5.write_text("....")
# path5.write_bytes()

# source = Path("ecommerce/__init__.py")
# target = Path() / "__init__.py"
# shutil.copy(source, target) - This is a quicker and easier way to copy the contents of a file to a new location


############################################## Working with Zip Files ###############################################

# with ZipFile("files.zip", "w") as zip: - Creates or overwrites a ZIP archive
#   for path in Path("ecommerce").rglob("*.*") - Finds all files in the ecommerce directory and sup directories that match the desired pattern
#       zip.write(path) - Adds each found file to the ZIP archive

# with ZipFile("files.zip") as zip: - Goes through the zip file and lists all of the files in the particular zip file
#   print(zip.namelist()) - Prints the names of the files in the directory
#   info = zip.getinfo("ecommerce/__init__.py") - Gets info on the particular file from the directory
#   print(info.file_size) - Prints the file size
#   print(info.compress_size) - Prints the compress size
#   zip.extractall("extract") - Extracts all the contents into a new directory called extract


######################################## Working with CSV Files ################################################

# with open("data.csv", "w") as file:
#   writer = csv.writer(file)
#   writer.writerow(["ransaction_id", "product_id", "price"])
#   writer.writerow([1000, 1, 5])
#   writer.writerow([1001, 2, 15])

# with open("data.csv") as file:
#   reader = csv.reader(file)
#   print(list(reader))
#   for row in reader:
#       print(row)


######################################### Working with JSON Files ########################################

# movies = [
#   {"id": 1, "title": "Terminator", "year": 1989},
#   {"id": 2, "title": "Kindergarten Cop", "year": 1993}
# ]

# data = json.dumps(movies)
# print(data)

# Path("movies.json").write_text(data)

# data = Path("movies.json").read_text()
# movies = json.loads(data)
# print(movies)


################################## Working with a SQLite Database #########################################

# movies = json.loads(Path("movies.json").read_text())
# print(movies)

# with sqlite3.connect("db.sqlite3") as conn:
#   command = "INSERT INTO Movies VALUES(?, ?, ?)"
#   for movie in movies:
#       conn.execute(command, tuple(movie.values()))
#   conn.commit()

# with sqlite3.connect("db.sqlite3") as conn:
#   command = "SELECT * FROM Movies"
#   cursor = conn.execute(command)
#   for row in cursor:
#       print(row)
#   movies = cursor.fetchall()
#   print(movies)


###################################### Working with Timestamps #############################################

print(time.time())


def send_emails():
    for i in range(10000):
        pass


start = time.time()
send_emails()
end = time.time()
duration1 = end - start
print(duration1)


####################################### Working with DateTimes ################################################

dt = datetime(2018, 1, 1)
dt = datetime.now()
dt = datetime.strptime("2018/01/01", "%Y/%m/%d")
dt = datetime.fromtimestamp(time.time())
print(dt)

print(f"{dt.year}/{dt.month}")
print(dt.strftime("%Y/%m"))


########################################## Working with Time Deltas ############################################

dt1 = datetime(2018, 1, 1) + timedelta(days=1, seconds=1000)
dt2 = datetime.now()

duration2 = dt2 - dt1
print(duration2)
print("days", duration2.days)
print("seconds", duration2.seconds)
print("total_seconds", duration2.total_seconds())


############################################## Generating Random Values ################################################

print(random.random())
print(random.randint(1, 10))
print(random.choice([1, 2, 3, 4]))
print(random.choices([1, 2, 3, 4], k=2))
print("".join(random.choices(string.ascii_letters + string.digits, k=10)))

print(string.ascii_letters)
print(string.ascii_uppercase)
print(string.ascii_lowercase)
print(string.digits)

numbers = [1, 2, 3, 4]
random.shuffle(numbers)
print(numbers)


################################################# Opening the Browser ################################################

print("Deployment completed")
# webbrowser.open("http://google.com")



############################################# Sending Emails #################################################

# message = MIMEMultipart()
# message["from"] = "Mosh Hamedani"
# message["to"] = "testuser@codewithmosh.com"
# message["subject"] = "This is a test"
# message.attach(MIMEText("Body"))
# message.attach(MIMEImage(Path("mosh.png").read_bytes()))
# with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
#     smtp.ehlo()
#     smtp.starttls()
#     smtp.login("testuser@codewithmosh.com", "todaytheskyisblue")
#     smtp.send_message(message)
#     print("Sent...")


############################################# Templates ##################################################

# template = Template(Path("template.html").read_text())
# message = MIMEMultipart()
# message["from"] = "Mosh Hamedani"
# message["to"] = "testuser@codewithmosh.com"
# message["subject"] = "This is a test"
# body = template.substitute({"name:": "John"})
# message.attach(MIMEText(body, "html"))
# message.attach(MIMEImage(Path("mosh.png").read_bytes()))
# with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
#     smtp.ehlo()
#     smtp.starttls()
#     smtp.login("testuser@codewithmosh.com", "todaytheskyisblue")
#     smtp.send_message(message)
#     print("Sent...")



#################################### Command-line Arguments #######################################

# print(sys.argv)
# if len(sys.argv) == 1:
#   print("USAGE: python3 app.py <password>")
# else:
#   password = sys.argv[1]
#   print("Password", password)


####################################### Running External Programs #################################

# try:
#     completed = subprocess.run(["ls", "-l"],capture_output=True, text=True, check=True)
#     print(type(completed))
#     print("args", completed.args)
#     print("returncode", completed.returncode)
#     print("stderr", completed.stderr)
#     print("stdout", completed.stdout)
# except subprocess.CalledProcessError as ex:
#     print(ex) 

