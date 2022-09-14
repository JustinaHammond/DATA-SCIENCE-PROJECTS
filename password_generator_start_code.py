"""
    Password Generator Project
    input:  password length
            Number of Digits
            Number of Symbols
    
    output: password (as string)
"""
####################################################################################################
######################## DO NOT CHANGE THIS SECTION OF THE CODE ####################################
# importing the relevant modules
import string
import random

# List of all lowercase and uppercase characters in Python
all_alphabets = list(string.ascii_letters)
print(f'these are all the alphabets of the English language {all_alphabets}')

all_digits = list(string.digits)
print(f'these are the numbers in English Language {all_digits}')

all_symbols = list(string.punctuation)
print(f'these are the symbols in English Language {all_symbols}')

#########################################################################################################



####################################### TYPE YOU CODE IN HERE! ##########################################
# Ask user for how many letters they would like in their password and cast to integer and store as no_of_letters
no_of_letters = int(input('How many letters would you like in your password? '))

# Ask user for how many symbols they would like in their password and cast to integer and store as no_of_symbols
no_of_symbols = int(input('How many symbols would you like in your password? '))

# Ask user for how many digits they would like in their password and cast to integer and store as no_of_digits
no_of_digits = int(input('How many numbers would you like in your password? '))

# Set Accumulator for Password Characters List
password_character_list = []

# Get the random letter for the password
# Randomly Select the characters
for number in range(no_of_letters):
#       select a random characer from list of alphabets and append to the password characters list 
    random_letter = random.choice(all_alphabets)
    password_character_list.append(random_letter)

print(password_character_list)

# Set Accumulator for the Number of Symbols List
password_symbol_list = []

# Randomly Select the characters
for number in range(no_of_symbols):
#       select a random symbol from list of symbols and append to the password symbols list 
    random_symbol =random.choice(all_symbols)
    password_symbol_list.append(random_symbol)

print(password_symbol_list)

# Get the Random Digits for the password
# Set Accumulator for the Number of Digits List
password_digit_list = []

# Randomly Select the characters
for number in range(no_of_digits):
#       select a random digit from list of digits and append to the password digits list 
    random_digit =random.choice(all_digits)
    password_digit_list.append(random_digit)

print(password_digit_list)

# Add the lists to get the final_password_list and shuffle the final_password_list
final_password_list = password_character_list + password_symbol_list + password_digit_list

# Shuffle the final_password_list
random.shuffle(final_password_list)

print(final_password_list)

# To shuffle, items in a list https://www.w3schools.com/python/ref_random_shuffle.asp 

# Now that we have our password in a list lets change that to a string then print it


# accumulator for string_password
string_password = []

for character in final_password_list:
#       append the character to the string_password
   string_password = ' '.join(map(str,final_password_list))
          
# Print the string password
print(string_password)