#!/home/rhyme/penv/bin/python3

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding


import sys, os

if (len(sys.argv)) != 2:
    print ('Usage: ./encrypt.py original_filename')
    exit(-1)

with open(sys.argv[1], 'rb') as org_file:
    org_data=org_file.read()

pub_pem=os.environ.get('PUB_PEMK')
with open(pub_pem,'rb') as pub_key_file:
    public_key=serialization.load_pem_public_key(
        pub_key_file.read()
    )
encrypted=public_key.encrypt(
    org_data,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
with open(sys.argv[1]+'.encrypted','wb') as fh:
    fh.write(encrypted)