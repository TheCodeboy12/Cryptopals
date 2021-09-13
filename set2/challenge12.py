import random

from Crypto import Cipher
from challenge1 import PKCS
from Crypto.Cipher import AES
import base64
import pdb

# Good article for this challenge : https://braincoke.fr/write-up/cryptopals/cryptopals-byte-a-time-ecb-decryption-simple/
text='''Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg
aGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq
dXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUg
YnkK'''
decoded=base64.b64decode(text) #decoding the text above
message=b'I love ice cream with PiTA!!! lol'
key=random.randbytes(16)
unknown=message+decoded

'''
1. Feed identical bytes of your-string to the function 1 at a time 
--- start with 1 byte ("A"), then "AA", then "AAA" and so on. Discover the block size of the cipher. You know it, but do this step anyway. 
'''
def detectECB(ciphertext:bytes,keysize:int):
    '''ECB will always produce the same text with the same key as opposed to CBC'''
    #We will break the ciphertext into keysize chunks and check where we see the most duplicates
    chunks=[ciphertext[i:i+keysize] for i in range(0,len(ciphertext),keysize)]
    #assert len(chunks)>2
    if len(set(chunks))<len(chunks): #This is ECB
        return True

def oracle(message:bytes):

    #appending 5-10 bytes to the beginning and end
    if len(message)%16 != 0: #Check if it needs padding
        message=PKCS(message, 16) #Padding the message to 16
    key=random.randbytes(16) #generating a random key
    cipher=AES.new(key,AES.MODE_ECB)
    encryptedMessage=cipher.encrypt(message)

    return encryptedMessage

def main():
    text='''Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg
    aGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq
    dXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUg
    YnkK'''
    decoded=base64.b64decode(text) #decoding the text above
    message=b'I love ice cream with PiTA!!! lol'
    key=random.randbytes(16)
    unknown=message+decoded
    pdb.set_trace()
    print(oracle(unknown)[1])
    return oracle(unknown[1])

if __name__ == "__main__":
    print(main())
