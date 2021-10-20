#!C:\python36\Python36-32\python.exe
import cgitb
import cgi
import random
import string
cgitb.enable()
print("Content-Type: text/html")    # HTML is following
print()                             # blank line, end of headers
form = cgi.FieldStorage()
characters_number = form.getvalue('cn')

s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)

random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)
# print(s1,s2,s3,s4)

while True:
    try:
        characters_number = int(characters_number)
        if characters_number < 6 :
            print("<p id='error-6' name='error-6'> you need at least 6 characters . </p>")
            print("<form action='generate.py' method='POST' enctype='multipart/form-data'><input type='text' id='cn' name='cn' placeholder='Enter how many characters'><input type='submit' id='submit' name='submit' value='Generate'></form>")
        else :
            break
    except:
        print("<p id='error-6' name='error-6'>Please enter numbers only</p>")
        print("<form action='generate.py' method='POST' enctype='multipart/form-data'><input type='text' id='cn' name='cn' placeholder='Enter how many characters'><input type='submit' id='submit' name='submit' value='Generate'></form>")
part1 = round(characters_number * (30/100))
part2 = round(characters_number * (20/100))

password = []

for i in range(part1):
    password.append(s1[i])
    password.append(s2[i])

for i in range(part2):
    password.append(s3[i])
    password.append(s4[i])
password = "".join(password[0:])
print(password)