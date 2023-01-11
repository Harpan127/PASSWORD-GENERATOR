import random

string = ""     # Variable will hold all characters

# Adds all characters and numbers to string

for i in range(ord("!"), ord('z') + 1):
    string += str(chr(i))

# Creates a random length between 12-20

len_of_pass = random.randrange(12, 20)

# Creates the password from the string

password = "".join(random.sample(string, len_of_pass))
print(password)
