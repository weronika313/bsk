import math

def encrypt_columnar_transposition_a(message :str, key :str) -> str:

    key_table :list[int] = []
    for column_number in range(len(key)):
        if key[column_number] != '-':
            key_table.append(int(key[column_number]))

    row_number = math.ceil(len(message)/ len(key_table))
    message_table = [[' ' for i in range(len(key_table))] for j in range(row_number)]
    letter_index = 0
    for i in range(row_number):
        for j in range(len(key_table)):
            if letter_index < len(message):
                message_table[i][j] = message[letter_index]
                letter_index+=1

    encrypted_message: str = ""
    for j in range(row_number):
        for i in key_table:
            if message_table[j][i-1] != ' ':
                encrypted_message += message_table[j][i-1]

    return encrypted_message


def decrypt_columnar_transposition_a(message :str, key :str) -> str:

    key_table :list[int] = []
    for column_number in range(len(key)):
        if key[column_number] != '-':
            key_table.append(int(key[column_number]))

    row_number = math.ceil(len(message)/ len(key_table))
    letters_in_last_row = len(message) % len(key_table)
    message_table = [[' ' for i in range(len(key_table))] for j in range(row_number)]
    letter_index = 0

    for j in range(row_number):
        for i in key_table:
            if letter_index < len(message):
                if j == row_number-1 and i>letters_in_last_row:
                    continue
                else:
                    message_table[j][i-1] = message[letter_index]
                    letter_index +=1
            else:
                break

    decrypted_message: str = ""

    for i in range(row_number):
        for j in range(len(key_table)):
            if message_table[i][j] != ' ':
                decrypted_message += message_table[i][j]

    return decrypted_message


def encrypt_columnar_transposition_b(message: str, key: str) -> str:
    message = (message.replace(" ", "")).upper()
    key_sequence = create_key_sequence(key)

    row_number = math.ceil(len(message)/ len(key_sequence))
    message_table = [[' ' for i in range(len(key_sequence))] for j in range(row_number)]
    letter_index = 0
    for i in range(row_number):
        for j in range(len(key_sequence)):
            if letter_index < len(message):
                message_table[i][j] = message[letter_index]
                letter_index+=1


    encrypted_message: str = ""
    for j in range(1, len(key_sequence)+1):
        for i in range(row_number):
            encrypted_message += message_table[i][key_sequence.index(j)]

    return encrypted_message


def decrypt_columnar_transposition_b(message: str, key: str) -> str:
    message = (message.replace(" ", "")).upper()
    key_sequence = create_key_sequence(key)

    row_number = math.ceil(len(message)/ len(key_sequence))
    letters_in_last_row = len(message)%len(key_sequence)
    message_table = [[' ' for i in range(len(key_sequence))] for j in range(row_number)]
    letter_index = 0

    for j in range(1, len(key_sequence)+1):
        for i in range(row_number):
            if letter_index < len(message):
                if i == row_number - 1 and j > letters_in_last_row:
                    continue
                else:
                    message_table[i][key_sequence.index(j)] = message[letter_index]
                    letter_index+=1

    decrypted_message: str = ""
    for i in range(row_number):
        for j in range(len(key_sequence)):
            decrypted_message += message_table[i][j]

    return decrypted_message


def create_key_sequence(key: str) -> list[int]:
    key_sequence :list[int] = ['1' for i in range(len(key))]
    temp :int = 1

    for i in range(0, 25):
        for j in range(0, len(key)):
            if key[j] == chr(ord('A') + i):
                key_sequence[j] = temp
                temp+=1

    return key_sequence









