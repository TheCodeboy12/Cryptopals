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

from Crypto import Cipher
from Crypto.Cipher import AES  #relies on https://pycryptodome.readthedocs.io/en/latest/src/cipher/cipher.html
from challenge2 import CBC_encrypt
import random
from challenge1 import PKCS
import pdb

def xor(message:bytes,message2:bytes):
    assert len(message)==len(message2),'Not same lengh messages'
    return bytes([x^y for x,y in zip(message,message2)])
def detectECB(message:bytes,keysize:int):
    '''ECB will always produce the same text with the same key as opposed to CBC'''
    assert len(message)%16==0,'Message is not good with the keysize'
    chunks=[message[i:i+keysize] for i in range(0,len(message),keysize)]
    pdb.set_trace()
    if len(message)>sum([len(set(x)) for x in chunks]):
        return True
    else: 
        return False
def CBC_encrypt(message:bytes,key:bytes,IV:bytes=random.randbytes(16)):
    cipher=AES.new(key,AES.MODE_ECB)
    bytesize=16
    message=PKCS(message, bytesize)
    #Breaking into chunks of bytesize
    chunks=[message[i:i+bytesize] for i in range(0,len(message),bytesize)]
    for chunk in chunks:
        if chunks.index(chunk)==0:
            chunks[0]=cipher.encrypt(xor(chunk,IV)) #encrypting using the Xor of the IV and chunk0
        else:
            chunks[chunks.index(chunk)]=cipher.encrypt(bytes([x^y for x,y in zip(chunk,chunks[chunks.index(chunk)-1])]))
    return b''.join(chunks)

#Write a function to generate a random AES key; that's just 16 random bytes.
def generate_random_bytes(keylen=16):
   return  bytes([random.randint(0,255) for n in range(keylen)])

def encryptECB(message:bytes,key:bytes):
    cipher=AES.new(key,AES.MODE_ECB)
    return cipher.encrypt(message)

def oracle(message:bytes):

    #appending 5-10 bytes to the beginning and end
    message=PKCS(generate_random_bytes(random.randint(5,10))+message+generate_random_bytes(random.randint(5, 10)),16)

    key=generate_random_bytes(16)
    chooser=random.randint(0,1)
    encrypted=b''
    if chooser==0: 
        #we encrypt with ECB
        encrypted= encryptECB(message,key)
    elif chooser==1:
        #We use CBC
        encrypted= CBC_encrypt(message,key)

    if detectECB(message,16)==True:
        print('This is ECB')
    else:
        print('This is CBC')
    
    return chooser


print(oracle(b'lol I love '))


# '''
# My idea: 
# since we pad the plain text with some random bytes.
# IF I encrypt with ECB I will always find that plain text as opposed to encrypting with CBC.
# With CBC we also have the initialazation vector 

# Anyways, in ECB bytes will always repeat in messages that are encrypted that are biggger then the keysize
# encryptECB(key,b'A'*32)

# For exmple: encryptECB(key,b'A'*32) =>
# b'\xac\xba\x1d`\x12\xd6bR\xe3dKg\xd80*\xe0\xac\xba\x1d`\x12\xd6bR\xe3dKg\xd80*\xe0'
# And I can see that if we break it into chunks the size of the keysize (16) we get two equal chunks


# CBC is different
# CBC_encrypt(b'A'*32,key) = >
# b'\xac\xba\x1d`\x12\xd6bR\xKg\e3dxd80*\xe0s\x19\xf2\xd8\xa4xX\xae*7\xd5qx[\x89\xc7'

# Which because of the nature of that method does not produce duplicates almost at all.
# '''