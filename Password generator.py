import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

l_part=[]
s_part=[]
n_part=[]
for i in range (nr_letters):
    l_part.append(random.choice(letters))
for i in range (nr_symbols):
    s_part.append(random.choice(symbols))
for i in range (nr_numbers):
    n_part.append(random.choice(numbers))
password = l_part+s_part+n_part
len_password=len(password)
rand_pass=[]
for k in range(len_password):
    rand_pass.append(random.choice(password))
rand_pass=''.join(rand_pass)
print(rand_pass)