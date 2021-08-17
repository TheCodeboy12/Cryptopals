#set[5]


def repeating_key_XOR(text:bytes,key:bytes):
    cipher=bytes(cipher,'ascii')
    return b''.join([bytes([x^y]) for x,y in zip(text,cipher*len(text))])

def decrypt(message,key):
    return b''.join([bytes([x^y]) for x,y in zip(message,key)])
    
def main():
    text=b"hi gali ma kore lama lo ahalt avatiah"
    cipher='Sillam'
    print(f'\nEncrypted: {repeating_key_XOR(text,cipher)}')

    #print(f'Decrypted : {decrypt(repeating_key_XOR(text,cipher), cipher)}\n')


if __name__ == '__main__':
        main()


