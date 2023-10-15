plaintext = input("Please enter your word: ")
n = int(input("Enter your level of encryption: "))

def encrypt_message(plaintext, n):
    encrypted_message = ""

    for i in range(len(plaintext)):
        char = plaintext[i]

        if char == " ":
            encrypted_message += " "
        elif (char.isupper()):
            encrypted_message += chr((ord(char) + n-65) % 26+65)
        else:
            encrypted_message += chr((ord(char) + n-97) % 26+97)

    return encrypted_message

print(encrypt_message(plaintext, n))

