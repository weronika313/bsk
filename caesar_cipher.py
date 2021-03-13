FIRST_CHAR = 97
NUMBER_OF_CHARS = 26
FIRST_UPPER_CHAR = 65
LAST_UPPER_CHAR = 90


def encrypt_caesar_cipher(message: str, key: int) -> str:
    isUpper: bool = False
    decrypted_message = ""

    for i in range(len(message)):
        c = ord(message[i])
        if c == 32:
            decrypted_message += " "
            continue

        if c >= FIRST_UPPER_CHAR and c <= LAST_UPPER_CHAR:
            isUpper = True
            c += FIRST_CHAR - FIRST_UPPER_CHAR

        c = ((c - FIRST_CHAR + key) % (NUMBER_OF_CHARS)) + FIRST_CHAR

        if isUpper:
            c -= FIRST_CHAR - FIRST_UPPER_CHAR
            isUpper = False

        decrypted_message += chr(c)

    return decrypted_message


def decrypt_caesar_cipher(message: str, key: int) -> str:
    key = NUMBER_OF_CHARS - key
    return encrypt_caesar_cipher(message, key)
