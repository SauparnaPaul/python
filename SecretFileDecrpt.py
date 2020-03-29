import os
from cryptography.fernet import Fernet
key = b'' # Use one of the methods to get a key (it must be the same as used in encrypting)
input_file = input("File name to Decrypt: ")
output_file = input_file.split()[0]+".jpg"

file = open('key.key', 'rb')
key = file.read() # The key will be type bytes
file.close()

with open(input_file, 'rb') as f:
    data = f.read()
os.remove(input_file)
fernet = Fernet(key)
encrypted = fernet.decrypt(data)

with open(output_file, 'wb') as f:
    f.write(encrypted)

# You can delete input_file if you want
