'''
 Now that you have ECB and CBC working:
Write a function to generate a random AES key; that's just 16 random bytes.
Write a function that encrypts data under an unknown key --- that is, a function that generates a random key and encrypts under it.
The function should look like:
encryption_oracle(your-input)
    => [MEANINGLESS JIBBER JABBER]

Under the hood, have the function append 5-10 bytes (count chosen randomly) before the plaintext and 5-10 bytes after the plaintext.

Now, have the function choose to encrypt under ECB 1/2 the time, and under CBC the other half (just use random IVs each time for CBC). Use rand(2) to decide which to use.

Detect the block cipher mode the function is using each time. You should end up with a piece of code that, pointed at a block box that might be encrypting ECB or CBC, tells you which one is happening. 
'''

from Crypto.Cipher import AES  #relies on https://pycryptodome.readthedocs.io/en/latest/src/cipher/cipher.html
from challenge2 import CBC_encrypt
import random

#Write a function to generate a random AES key; that's just 16 random bytes.
def generate_random_bytes(keylen=16):
   return  bytes([random.randint(0,255) for n in range(keylen)])

def encryptECB(key:bytes,message:bytes):
    cipher=AES.new(key,AES.MODE_ECB)
    return cipher.encrypt(message)

def oracle(message:bytes):
    #appending 5-10 bytes to the beginning and end
    message=generate_random_bytes(random.randint(5,10))+message+generate_random_bytes(random.randint(5, 10))

    return message


print(oracle(b'lol I love choco'))


