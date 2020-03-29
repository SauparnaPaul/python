from cryptography.fernet import Fernet
import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

'''key = Fernet.generate_key()

file = open('key.key', 'wb')
file.write(key) # The key is type bytes still
file.close()

file = open('key.key', 'rb')
key = file.read() # The key will be type bytes
file.close()'''



password_provided = input("Password: ") # This is input in the form of a string
password = password_provided.encode() # Convert to type bytes
salt = b'salt_' # CHANGE THIS - recommend using a key from os.urandom(16), must be of type bytes
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
)
key = base64.urlsafe_b64encode(kdf.derive(password)) # Can only use kdf once

file = open('key.key', 'wb')
file.write(key) # The key is type bytes still
file.close()

#key = b'' # Use one of the methods to get a key (it must be the same when decrypting)
input_file = input("File name: ")
output_file = input_file.split()[0]+'.encrypted'

with open(input_file, 'rb') as f:
    data = f.read()
os.remove(input_file)
fernet = Fernet(key)
encrypted = fernet.encrypt(data)

with open(output_file, 'wb') as f:
    f.write(encrypted)

# You can delete input_file if you want


