'''
Implement CBC mode
CBC mode is a block cipher mode that allows us to encrypt irregularly-sized messages, despite the fact that a block cipher natively only transforms individual blocks.
In CBC mode, each ciphertext block is added to the next plaintext block before the next call to the cipher core.
The first plaintext block, which has no associated previous ciphertext block, is added to a "fake 0th ciphertext block" called the initialization vector, or IV.
Implement CBC mode by hand by taking the ECB function you wrote earlier, making it encrypt instead of decrypt (verify this by decrypting whatever you encrypt to test), and using your XOR function from the previous exercise to combine them.
The file here is intelligible (somewhat) when CBC decrypted against "YELLOW SUBMARINE" with an IV of all ASCII 0 (\x00\x00\x00 &c) 
'''

#relies on https://pycryptodome.readthedocs.io/en/latest/src/cipher/cipher.html
from Crypto.Cipher import AES
import base64
import hashlib
import pdb
from challenge1 import PKCS
message=b'hello world yeah I love eating pizza, freies and other things with my buds'
message=PKCS(message,80)

#chunks=[message[i:i+bytesize] for i in range(0,len(message),bytesize)]
key=b'GABE THE KING!!!'
#key=AES.new(key,AES.MODE_ECB)
def CBC_encrypt(message:bytes, key:bytes):
    key=AES.new(key,AES.MODE_ECB)
    bytesize=16
    #Breaking into chunks of bytesize
    chunks=[message[i:i+bytesize] for i in range(0,len(message),bytesize)]
    for chunk in chunks:
        if chunks.index(chunk)==0:
            chunks[0]=key.encrypt(chunk) #initialization vector
        else:
            chunks[chunks.index(chunk)]=key.encrypt(bytes([x^y for x,y in zip(chunk,chunks[chunks.index(chunk)-1])]))
    return b''.join(chunks) 

encrypted_message=CBC_encrypt(message,key)
print (f'The message is:\n {message}\n')
print(f'The CBC encrypted message:\n{encrypted_message}')