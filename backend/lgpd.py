from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

import sys
import binascii
import base64
import os

password="btg"
val="59508089684"

def get_key(password):

    salt = os.urandom(16)
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(),length=32,salt=salt,iterations=100,backend=default_backend())
    key=base64.urlsafe_b64encode(kdf.derive(password))
    return (key,salt)

if (len(sys.argv)>1):
	val=sys.argv[1]

if (len(sys.argv)>2):
	password=str(sys.argv[2])

(key,salt) = get_key(password.encode())
cipher_suite = Fernet(key)
cipher_text = cipher_suite.encrypt(val.encode())
plain_text = cipher_suite.decrypt(cipher_text)