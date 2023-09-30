import random

# Define a string containing characters that can be part of the password.
letters = 'absdehghABCDEFG'


# Function to create a random password.
def create_password(letters):
    password = ''  # Initialize an empty string to store the password.

    # Generate a password of length 5.
    for i in range(5):
        number = random.randint(0, 9)  # Generate a random number between 0 and 9.
        # Append a random character from the 'letters' string and the random number to the password.
        password += (random.choice(letters) + str(number))

    return password  # Return the generated password.


# Print a random password created using the 'create_password' function.
print(create_password(letters))

# Define a list of integers ranging from 0 to 9 and ASCII values for characters ranging from 'A' to 'z'.
listas = list(range(0, 9)) + list(range(65, 122))

# Initialize an empty string to store the password.
password = ''

# Generate a password of length 20.
for i in range(20):
    num = random.choice(listas)  # Choose a random number from 'listas'.

    if num <= 9:
        password += str(num)  # If the number is less than or equal to 9, add it as a digit to the password.
    else:
        password += chr(num)  # If the number is greater than 9, add its corresponding character to the password.

# Print the final password.
print(password)
