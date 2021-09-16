import random

from Crypto import Cipher
from challenge1 import PKCS
from Crypto.Cipher import AES
import base64
import pdb
import string
import sys
import time
# Good article for this challenge : https://braincoke.fr/write-up/cryptopals/cryptopals-byte-a-time-ecb-decryption-simple/

def progressbar(it, prefix="", size=60, file=sys.stdout):
    count = len(it)
    def show(j):
        x = int(size*j/count)
        file.write("%s[%s%s] %i/%i\r" % (prefix, "#"*x, "."*(size-x), j, count))
        file.flush()        
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    file.write("\n")
    file.flush()
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
    b64text=base64.b64encode(b'NU LAMA LO')
    decoded=base64.b64decode(b64text) #decoding the text above
    message=b'A'*32 #To attack the cipher and fill out 2 blocks
    key=b'\x99\xc4\xfa\xd3\xf5%I\xc9{sG\xea\xd8r\xdc\x8f' #generated random key
    #1. Finding the blocksize #done
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
    print('Is this ECB ? ',detectECB(oracle(message+decoded, key), blocksize)) #Done

    #attacking with a dictionary brute force
    d={k:v for k,v in zip([oracle(b'A'*15+bytes([n]),key) for n in range(0,256)],range(0,256))}
    
    print(f'Ciper text is:{oracle(decoded,key)}\n')
    q=input('Would you like to brute force this cipher using dictionary attack? Y/N:')
    
    if q.lower()=='y':
        print('Attacking ECB encryption using dictionary attack...\n')
        for i in progressbar(range(20), "On it brah...: ", 40):
            time.sleep(0.1) # any calculation you need
        print(f"decrypted text is: {b''.join([bytes([d[oracle(b'A'*15+bytes([decoded[n]]),key)]]) for n in range(0,len(decoded))])}")
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
    main()
