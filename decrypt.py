#!/home/rhyme/penv/bin/python3

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

import os, sys


if (len(sys.argv)) != 2:
    print ('Usage: ./decrypt.py original_filename')
    exit(-1)

with open(sys.argv[1]+'.encrypted','rb') as file:
    encrypted=file.read()

priv_pem=os.environ.get('PEMK')
with open(priv_pem,'rb') as key_file:
    private_key=serialization.load_pem_private_key(
        key_file.read(),
        password=None
    )

decrypted=private_key.decrypt(
    encrypted,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

with open(sys.argv[1]+'.decrypted','wb') as fh:
    fh.write(decrypted)