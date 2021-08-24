#Implement PKCS#7 padding
def PKCS(message:bytes,blocksize:int):
    assert blocksize>2 or blocksize>255, 'Block size must be between 2 and 255 bytes'
    padsize=blocksize-(len(message)%blocksize)
    padding=bytes([padsize]*padsize)
    return message+padding

def main():
    key=b'YELLOW SUBMARINE'
    print(PKCS(key,16))
if __name__ == '__main__':
    main()
