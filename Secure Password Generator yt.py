


import secrets
import string

def generate_password(length=16):
  """
  Generates a random, cryptographically secure password of the specified length.

  Args:
      length (int, optional): The desired length of the password. Defaults to 16.

  Returns:
      str: The generated random password.
  """

  # Define character sets for the password
  lowercase = string.ascii_lowercase
  uppercase = string.ascii_uppercase
  digits = string.digits
  punctuation = string.punctuation

  # Combine all character sets
  all_chars = lowercase + uppercase + digits + punctuation

  # Use secrets.choice for cryptographically secure randomness
  password = ''.join(secrets.choice(all_chars) for i in range(length))

  return password

# Generate a password with default length (16 characters)
password = generate_password()
print(f"Your random password is: {password}")

# Optionally, generate a password with a custom length
custom_length = 20
custom_password = generate_password(custom_length)
print(f"Your custom password with length {custom_length} is: {custom_password}")
