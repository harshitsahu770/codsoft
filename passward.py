# passward genrator
import random
import string

print("Welcome to the PyPassword Generator!")

letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

nr_letters = int(input("How many letters would you like in your password : ")) 
nr_numbers = int(input("How many numbers would you like? : "))
nr_symbols = int(input("How many symbols would you like :"))

password_list = []

for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

for char in range(1, nr_numbers + 1):
    password_list.append(random.choice(numbers))

for char in range(1, nr_symbols + 1):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)

password = ''.join(password_list)

print(f"Your random password to use is: {password}")