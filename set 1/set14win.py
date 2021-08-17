import pdb
import string
#import pdb
hexushesh=[x[:60] for x in open('texts.txt').readlines()]
hexush=['1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736']
#charlist2='abcdefghijklmnopqrstuvwxyz'
#charlist2=string.ascii_letters
ETAOIN='ETAOINSHRDLCUMWFGYPBVKJXQZ'
#def single_byte_XOR_final(hexush):

def single_byte_XOR_final(hexx):
    #hexx is a single hex
    db={hexx:[]}
    #first I turn the hex into bytes
    hex_bytes=bytes.fromhex(hexx)
    charlist2=[x for x in range(256)] #256 chars in unicode
    db[hexx]=[''.join([chr(byte^char) for byte,char in zip(hex_bytes,[char]*len(hex_bytes))]) for char in range(256)]
    
    return db
    '''checked how many times a charater occured and retuns a percrntage list of them'''
   # [[tuple([char,decrypted_text.count(char)/len(decrypted_text)*100]) for char in charlist2[:26]] for decrypted_text in decrypted_text_block]
def check_scores(sorted_text):
    occurance_english={
        'a': 8.2389258,    'b': 1.5051398,    'c': 2.8065007,    'd': 4.2904556,
        'e': 12.813865,    'f': 2.2476217,    'g': 2.0327458,    'h': 6.1476691,
        'i': 6.1476691,    'j': 0.1543474,    'k': 0.7787989,    'l': 4.0604477,
        'm': 2.4271893,    'n': 6.8084376,    'o': 7.5731132,    'p': 1.9459884,
        'q': 0.0958366,    'r': 6.0397268,    's': 6.3827211,    't': 9.1357551,
        'u': 2.7822893,    'v': 0.9866131,    'w': 2.3807842,    'x': 0.1513210,
        'y': 1.9913847,    'z': 0.0746517
        }
        #takes sorted text from dictionary_to_sorted_string and returns the score of the text based on the algorithm
    ETAOIN='ETAOINSHRDLCUMWFGYPBVKJXQZ'
    score=0
    for letter in sorted_text[-6:]:
        if letter in ETAOIN[-6:]:
            score+=1
    for letter in sorted_text[:6]:
        if letter in ETAOIN[:6]:
            score+=1
    return score
def dictionary_to_sorted_string(dictionary):
    #takes a dictionary and sorts it
    #Returns a sorted string
    return "".join(sorted(dictionary,key=dictionary.get,reverse=True)).upper()
def check_occ(value):
    charlist='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    occurance_english={}
    for char in charlist:
            occurance_english.update({char:(value.upper().count(char)*(len(value)))/100})
    return occurance_english
def sorted_text_converted(XORed_dict):
    #we add the score to each text in each dicionary
    # We 
    ETAOIN='ETAOINSHRDLCUMWFGYPBVKJXQZ'
    key=next(iter(XORed_dict.keys()))
    k=[check_scores(dictionary_to_sorted_string(check_occ(value))) for value in XORed_dict[key]]
    max_score=max(k)
    XORed_dict[key]=dict(zip(XORed_dict[key],k))
    
    
    for t,s in XORed_dict[key].items():
        if s==max_score:
           XORed_dict[key]={t:s}
    
    return XORed_dict
    #THIS FUNCTION WORKS BITCH!
#Code:


def main():

    
    decryptions={}
    for h in hexushesh:
        decryptions.update(sorted_text_converted(single_byte_XOR_final(h)))

    High_score=max([next(iter(set(item.values()))) for item in list(decryptions.values())])
    
    for dic in list(decryptions.values()):
        for t,s in dic.items():
            if s==High_score:
                print(f'This is most likely the unecnrypted text: {t} \n its score is: {s}')
    
    '''''
    decryptions is a dictionary which is built like this:
    {
        hex:{high_scorer:score}
        hex:{high_scorer:score}
        hex:{high_scorer:score}
        ... *326
    }
        
        !Here are some stuff to remember:
            decryptions[hex]=> {high_scorer:score} (dict)
            decryptions[hex][text]=> score (int)

        # My goal:
            1. Find the hex with the highest score.

    '''

if __name__ == '__main__':
        main()