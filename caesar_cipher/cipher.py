
def caesar(message, offset):
    alphabet_lowercase = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    encrypted_text = ''

    for char in message.lower():  # Make the message in lowercase
        if char == ' ':            # Space must be Space
            encrypted_text += char
        elif char.isupper():
            index = alphabet_uppercase.find(char)
            new_index = (index + offset) % len(alphabet_uppercase)
            encrypted_text += alphabet_uppercase[new_index]
        elif char.islower:
            index = alphabet_lowercase.find(char)
            new_index = (index + offset) % len(alphabet_lowercase)
            encrypted_text += alphabet_lowercase[new_index]
    return encrypted_text
