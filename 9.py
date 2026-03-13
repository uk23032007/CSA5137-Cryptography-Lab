def rot13(text):
    result = ""
    for c in text:
        if 'A' <= c <= 'Z':
            result += chr((ord(c) - 65 + 13) % 26 + 65)
        elif 'a' <= c <= 'z':
            result += chr((ord(c) - 97 + 13) % 26 + 97)
        else:
            result += c
    return result

text = input("Enter Text: ")

print("Cipher Text:", rot13(text))
