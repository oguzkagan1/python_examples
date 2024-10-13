import random
import string

# Define the set of characters
chars = " " + string.whitespace + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)  # Convert 'chars' to a list
key = chars.copy()  # Create a copy of 'chars' for the 'key' list

# Shuffle the characters in the 'key' list (used as encryption key)
random.shuffle(key)

# Print the character sets (optional, for debugging)
print(f"chars: {chars}")
print(f"key: {key}")

# ENCRYPTION process
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

# For each letter in the plain text, find its corresponding encrypted character
for letter in plain_text:
    index = chars.index(letter)  # Find the index of the letter in the 'chars' list
    cipher_text += key[index]  # Add the corresponding character from 'key' to cipher_text

print(f"Original message: {plain_text}")
print(f"Encrypted message: {cipher_text}")


# DECRYPTION process
cipher_text_input = input("Enter the message to decrypt: ")  # Input the encrypted message
decrypted_text = ""

# For each encrypted letter, find its corresponding original character
for letter in cipher_text_input:
    index = key.index(letter)  # Find the index of the letter in the 'key' list
    decrypted_text += chars[index]  # Add the corresponding character from 'chars' to decrypted_text

print(f"Encrypted message: {cipher_text_input}")
print(f"Decrypted message: {decrypted_text}")