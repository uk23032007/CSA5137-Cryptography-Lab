import string

plain = string.ascii_uppercase
key = "QWERTYUIOPASDFGHJKLZXCVBNM"

def encrypt(text):
    result = ""
    for c in text.upper():
        if c in plain:
            result += key[plain.index(c)]
        else:
            result += c
    return result

text = input("Enter Text: ")

print("Encrypted Text:", encrypt(text))
