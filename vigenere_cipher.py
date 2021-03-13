def encrypt_vigenere_cipher(message: str, key: str) -> str:
    message = message.upper()
    key = generate_key(message, key)
    j: int = 0
    k: int = 0
    decrypted_message: str = ""

    for i in message:
        if i == " " or i == "\n":
            j += 1
            continue

        decrypted_message += chr(((ord(message[j]) + ord(key[k])) % 26) + 65)
        j += 1
        k += 1
    return decrypted_message


def decrypt_vigenere_cipher(message: str, key: str):
    message = message.upper()
    key = generate_key(message, key)
    j: int = 0
    k: int = 0
    decrypted_message: str = ""

    for i in message:
        if i == " " or i == "\n":
            j += 1
            continue

        decrypted_message += chr((((ord(message[j]) - ord(key[k])) + 26) % 26) + 65)
        k += 1
        j += 1

    return decrypted_message


def generate_key(message: str, key: str) -> str:
    new_key: str = key
    while len(message) > len(new_key):
        new_key += key

    return new_key
