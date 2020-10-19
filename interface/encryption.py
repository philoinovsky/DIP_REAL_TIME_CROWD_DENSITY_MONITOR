from utilities import encryption, decryption
from cryptography.fernet import Fernet

path_pswd = '/home/user/dip/interface/credentials/db_sqlite3_bytes.bin'
path_pub_key = '/home/user/dip/interface/credentials/db_sqlite3_key_bytes.bin'

"""
# Encrypt password and store it into binary file
encrypted_data = encryption("", "dipmember-1")
public_key = encrypted_data["key"]
ciphered_text = encrypted_data["text"]

print("===================================")
print(public_key)
print("===================================")
print(ciphered_text)

with open(path_pswd, 'wb') as file_object:
    file_object.write(ciphered_text)

with open(path_pub_key, 'wb') as file_object:
    file_object.write(public_key)
"""

# Decrypt password from binary file
with open(path_pub_key, 'rb') as file_object:
    for line in file_object:
        key = line

with open(path_pswd, 'rb') as file_object:
    for line in file_object:
        encryptedpwd = line
uncipher_text = decryption(key, encryptedpwd)
print(bytes(uncipher_text["text"]).decode("utf-8"))
