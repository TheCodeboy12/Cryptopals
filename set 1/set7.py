#set7
#relies on https://pycryptodome.readthedocs.io/en/latest/src/cipher/cipher.html
from Crypto.Cipher import AES
import base64
import hashlib
message=b'hello world yeah'
key=b'YELLOW SUBMARINE'
cipher=AES.new(key,AES.MODE_ECB)
g=cipher.encrypt(message)
