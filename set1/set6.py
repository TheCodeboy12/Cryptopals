#My code: 
#set[6]
import base64
import pdb
#b64texts=[base64.b64decode(''.join(x.splitlines())) for x in open('6.txt').readlines()]
b64texts=base64.b64decode(open('6.txt').read())
#b64texts=b';\x00L\x0b\x00\x01:I\x01\rA\x06<\x1b\tL\r\x0c>\x08L\x00\x0eM2\x01\r\x00\x15M2\x1f\r\x18\x08\x0c;'

'''
https://cryptopals.com/static/challenge-data/6.txt 
It's been base64'd after being encrypted with repeating-key XOR.
Decrypt it.
'''
'''
1.Let KEYSIZE be the guessed length of the key; try values from 2 to (say) 40.
Write a function to compute the edit distance/Hamming distance between two strings. The Hamming distance is just the number of differing bits. 
The distance between: 
'''
#Do 1:
def find_distance(text1:bytes,text2:bytes):
    assert len(text2)==len(text2)
    distance=''.join([bin(x^y) for x,y in zip(text1,text2)]).count('1')
    return distance
    #This FUNCTION WORKS!
#DONE V
'''
2. For each KEYSIZE, take the first KEYSIZE worth of bytes, and the second KEYSIZE worth of bytes,
 and find the edit distance between them. Normalize this result by dividing by KEYSIZE. 
'''
def break_to_chunks(b64decoded:bytes):
    '''
    Takes the decoded b64 text and breaks it into byte sizes between 2-42 as suggested]
    '''
    data={}
    # data looks like this : {bytesize:chunks of the b64 decoded text}
    for bytesize in range(2,41):
        chunks=[b64texts[i:i+bytesize] for i in range(0,len(b64texts),bytesize)]
        if len(chunks[-1])!= bytesize:
            del chunks[-1]
        data.update({bytesize:chunks})
    return data
# DONE V

'''
For each KEYSIZE, take the first KEYSIZE worth of bytes, and the second KEYSIZE worth of bytes, 
and find the edit distance between them.
 Normalize this result by dividing by KEYSIZE.
'''
'''
The KEYSIZE with the smallest normalized edit distance is probably the key. 
You could proceed perhaps with the smallest 2-3 KEYSIZE values. 
Or take 4 KEYSIZE blocks instead of 2 and average the distances.
'''
def sort_dict(x:dict):
    return {k: v for k, v in sorted(x.items(), key=lambda item: item[1])}

def calc_avg_distace(chunks):
    keysize=len(chunks[0])
    data={} #data is {keysize:distance}
    #chunk01=find_distance(chunks[1], chunks[2]) /keysize
    #chunk23=find_distance(chunks[2], chunks[3]) /keysize
    #avg=sum([chunk01,chunk23])/4
    data.update({keysize:find_distance(chunks[1], chunks[2]) /keysize})
    return data
    

def most_common(lst):
    return max(set(lst), key=lst.count)
   
def single_byte_XOR_final(bytess):
    data={}
    for char in range(256):
        data.update({char:b''.join([bytes([byte^char]) for byte,char in zip(bytess,[char]*len(bytess))])})
    return data

def check_scores(b:bytes):
    b=b.lower()
    score=0
    occurance_english={
        'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
        'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
        'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
        'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
        'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
        'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
        'y': .01974, 'z': .00074, ' ': .13000
        }
    for byte in b:
        if chr(byte) in list(occurance_english.keys()):
            score+=occurance_english[chr(byte)]
    return score

def repeating_key_XOR(text:bytes,cipher):
    return b''.join([bytes([x^y]) for x,y in zip(text,cipher*len(text))])

def main():
    pass
if __name__ == '__main__':
    chunks=break_to_chunks(b64texts)
    avreges={}
    for bytesize in chunks.keys():
        #init the avregest dictionary
        avreges.update(calc_avg_distace(chunks[bytesize]))
    avreges=sort_dict(avreges)
    #first byte from each chunk
    keysize=list(avreges.keys())[1] #this needs fixing..
    key=b''
    
    transposed=[b''.join([bytes([byte[i]]) for byte in chunks[keysize]]) for i in range(keysize)]
    '''transposed=> Makes a list of bytes from each byte position based on the keysize (ACTS as the len of the range since every 
    text has the len of the keysize.'''
    print('decrypting..')
    for t in transposed:
        xor=single_byte_XOR_final(t)
        scores=[check_scores(x) for x in xor.values()]
        key+=bytes([scores.index(max(scores))])
        print(f'key: {key}')
        print(f'Decrypted text: \n{repeating_key_XOR(b64texts,key)}')
        print('\n------------------------------------------')

    print(f'\nThe key is: {key}\n\n Decrypted text: \n{repeating_key_XOR(b64texts,key)}')

        