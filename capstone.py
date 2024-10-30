#!/home/rhyme/penv/bin/python
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding


import sys, os

if (len(sys.argv)) != 2:
    print ('Usage: ./capstone.py news_alert')
    exit(-1)

# the first command line argument is the news alert data.
# Use the given code to encode the data into bytes:
org_alert = sys.argv[1].encode()

# Read the public key from the file into a variable
pub_pem=os.environ.get('PUB_PEMK')
# using the PUB_PEMK Environment Variable as the filename.
with open(pub_pem,'rb') as pub_key_file:
    public_key=serialization.load_pem_public_key(pub_key_file.read())
# encrypt the data
encrypted=public_key.encrypt(
    org_alert,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Read the private key from the file into a variable
priv_pem=os.environ.get('PEMK')
with open(priv_pem, 'rb') as key_file:
    private_key=serialization.load_pem_private_key(
        key_file.read(),
        password=None
)
# using the PEMK Environment Variable as the filename.
# replace the following line of code and decrypt 
# the encrypted alert using the private key and assign 
# the decrpted data to the variable decrypted.
decrypted=private_key.decrypt(
    encrypted,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# print the decrypted alert (given below).
# print(decrypted.decode())
print(decrypted.decode())

