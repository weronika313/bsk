def encrypt_message_rail_fence(message: str, key: int) -> str:
    encrypted_message: str = ""
    position: int = 0
    change: int = 1

    message_table = [["*" for i in range(0, len(message))] for j in range(0, key)]

    for i in range(len(message)):
        message_table[position][i] = message[i]
        position += change

        if position != key and position != -1:
            continue
        else:
            change *= -1
            position += change * 2

    for i in range(key):
        for j in range(len(message)):
            if not message_table[i][j] == "*":
                encrypted_message += message_table[i][j]

    return encrypted_message


def decrypt_message_rail_fence(encrypted_message: str, key: int) -> str:
    decrypted_message: str = ""
    k: int = -1
    row: int = 0
    col: int = 0
    x: int = 0

    message_table = [
        ["*" for i in range(0, len(encrypted_message))] for j in range(0, key)
    ]

    for i in range(len(encrypted_message)):
        message_table[row][col] = "#"
        if row == 0 or row == (key - 1):
            k *= -1

        row += k
        col += 1

    for i in range(key):
        for j in range(len(encrypted_message)):
            if message_table[i][j] == "#":
                message_table[i][j] = encrypted_message[x]
                x += 1

    row = 0
    col = 0
    k = -1

    for i in range(len(encrypted_message)):
        decrypted_message += message_table[row][col]
        if row == 0 or row == (key - 1):
            k *= -1

        row += k
        col += 1

    return decrypted_message
