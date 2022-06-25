import string
import random

characters = list(string.ascii_letters + string.digits + string.punctuation)

def generate_random_password():
	length = 16

	random.shuffle(characters)
	
	## picking random characters from the list
	password = []
	for i in range(length):
		password.append(random.choice(characters))

	random.shuffle(password)

	print("".join(password))

generate_random_password()