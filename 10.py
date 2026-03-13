def playfair_matrix(key):
    key = key.upper().replace("J","I")
    matrix = []
    used = []

    for c in key:
        if c not in used and c.isalpha():
            used.append(c)

    for c in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if c not in used:
            used.append(c)

    matrix = [used[i:i+5] for i in range(0,25,5)]

    print("Playfair Matrix:")
    for row in matrix:
        print(row)

key = input("Enter Key: ")

playfair_matrix(key)
