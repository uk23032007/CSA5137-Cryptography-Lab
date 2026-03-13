

def encrypt(text, a, b):
    result = ""
    for char in text.upper():
        if char.isalpha():
            x = ord(char) - 65
            result += chr(((a*x + b) % 26) + 65)
        else:
            result += char
    return result

def decrypt(cipher, a, b):
    result = ""
    a_inv = pow(a, -1, 26)  
    for char in cipher:
        if char.isalpha():
            x = ord(char) - 65
            result += chr(((a_inv*(x - b)) % 26) + 65)
        else:
            result += char
    return result

text = input("Enter Text: ")
a = int(input("Enter key a: "))
b = int(input("Enter key b: "))

enc = encrypt(text, a, b)
dec = decrypt(enc, a, b)

print("Encrypted:", enc)
print("Decrypted:", dec)
