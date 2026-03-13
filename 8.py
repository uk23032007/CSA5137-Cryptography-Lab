import string

plain = string.ascii_uppercase
cipher = "MNBVCXZLKJHGFDSAPOIUYTREWQ"

def encrypt(text):
    result = ""
    for c in text.upper():
        if c in plain:
            result += cipher[plain.index(c)]
        else:
            result += c
    return result

def decrypt(text):
    result = ""
    for c in text.upper():
        if c in cipher:
            result += plain[cipher.index(c)]
        else:
            result += c
    return result

text = input("Enter Text: ")

enc = encrypt(text)
dec = decrypt(enc)

print("Encrypted:", enc)
print("Decrypted:", dec)
