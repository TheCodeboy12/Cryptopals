#Implement PKCS#7 padding
def PKCS(thebyte:bytes,blocksize:int):
    assert blocksize>len(thebyte), 'blocksize is smaller or equal to the the len of bytes'
    pad=blocksize-len(thebyte)
    return thebyte+bytes([pad]*pad)

def main():
    key=b'YELLOW SUBMARINE'
    print(PKCS(key,155))

if __name__ == '__main__':
    main()
