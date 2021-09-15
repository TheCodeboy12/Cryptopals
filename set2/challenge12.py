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

def oracle(message:bytes,key:bytes):

    #appending 5-10 bytes to the beginning and end
    if len(message)%16 != 0: #Check if it needs padding
        message=PKCS(message, 16) #Padding the message to 16
    
    cipher=AES.new(key,AES.MODE_ECB)
    encryptedMessage=cipher.encrypt(message)

    return encryptedMessage

def detectECB(ciphertext:bytes,keysize:int):
    '''ECB will always produce the same text with the same key as opposed to CBC'''
    #We will break the ciphertext into keysize chunks and check where we see the most duplicates
    chunks=[ciphertext[i:i+keysize] for i in range(0,len(ciphertext),keysize)]
    #assert len(chunks)>2
    if len(set(chunks))<len(chunks): #This is ECB
        return True
    
    else:
        return False

def main():
    b64text='''Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg
    aGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq
    dXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUg
    YnkK'''
    decoded=base64.b64decode(b64text) #decoding the text above
    message=b'A'*32 #To attack the cipher and fill out 2 blocks
    key=b'\x99\xc4\xfa\xd3\xf5%I\xc9{sG\xea\xd8r\xdc\x8f' #generated random key
    #1. Finding the blocksize
    ciphertext=b''
    initsize=len(oracle(decoded,key)) #we add nothing to the encrypted message
    blocksize=None
    for size in range(0,128):
        plaintext=message[:size]+decoded
        ciphertext=oracle(plaintext,key)
        if len(ciphertext)>initsize:
            print(f'The blocksize is {len(ciphertext)-initsize}')
            blocksize=len(ciphertext)-initsize
            break
    
    #2. Detect ECB
    print('Is this ECB ? ',detectECB(oracle(message+decoded, key), blocksize))

    return None

def calc_blocksize(ciphertext:bytes):
    initsize=len(ciphertext)
    for blocksize in range(0,128):
        plaintext=message[:blocksize]+decoded
        ciphertext=oracle(plaintext,key)
        if len(ciphertext)>initsize:
            print(f'The blocksize is {len(ciphertext)-initsize}')
            break

if __name__ == "__main__":
    print(main())
