# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from view import BskApp
from columnar_transposition import encrypt_columnar_transposition_a, decrypt_columnar_transposition_a, encrypt_columnar_transposition_b, decrypt_columnar_transposition_b
root = BskApp()
root.mainloop()
key = 3
message = "CRYPTOGRAPHY"
encrypt_columnar_transposition_b("HERE IS A SECRET MESSAGE ENCIPHERED BY TRANSPOSITION", "CONVENIENCE")
decrypt_columnar_transposition_b("HECRN CEYI ISEP SGDI RNTO AAES RMPN SSRO EEBT ETIA EEHS", "CONVENIENCE")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
