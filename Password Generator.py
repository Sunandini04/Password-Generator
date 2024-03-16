import random 
import array 

PASSWORD_LENGTH = 16

NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
LOWER_CASE = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
              'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 
              'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 
              'z'] 

UPPER_CASE = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
              'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 
              'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 
              'Z'] 

SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', 
           '*', '(', ')', '<'] 

COMBINED_LIST = NUMBERS + UPPER_CASE + LOWER_CASE + SYMBOLS 

random_number = random.choice(NUMBERS) 
random_upper = random.choice(UPPER_CASE) 
random_lower = random.choice(LOWER_CASE) 
random_symbol = random.choice(SYMBOLS) 

temp_password = random_number + random_upper + random_lower + random_symbol 

for _ in range(PASSWORD_LENGTH - 4): 
    temp_password += random.choice(COMBINED_LIST) 

temp_pass_list = array.array('u', temp_password) 
random.shuffle(temp_pass_list) 

password = "" 
for char in temp_pass_list: 
    password += char 

print("Generated Password:", password)
