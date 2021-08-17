import string
hexush='1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
#charlist2='abcdefghijklmnopqrstuvwxyz'
charlist2=string.ascii_letters
ETAOIN='ETAOINSHRDLCUMWFGYPBVKJXQZ'


occurance_english={
        'a': 8.2389258,    'b': 1.5051398,    'c': 2.8065007,    'd': 4.2904556,
        'e': 12.813865,    'f': 2.2476217,    'g': 2.0327458,    'h': 6.1476691,
        'i': 6.1476691,    'j': 0.1543474,    'k': 0.7787989,    'l': 4.0604477,
        'm': 2.4271893,    'n': 6.8084376,    'o': 7.5731132,    'p': 1.9459884,
        'q': 0.0958366,    'r': 6.0397268,    's': 6.3827211,    't': 9.1357551,
        'u': 2.7822893,    'v': 0.9866131,    'w': 2.3807842,    'x': 0.1513210,
        'y': 1.9913847,    'z': 0.0746517
        }


def single_byte_XOR_final1(hexx):
    #hexx is a single hex
    db={hexx:[]}
    #first I turn the hex into bytes
    hex_bytes=bytes.fromhex(hexx)
    
    charlist2=[bytes(char,'ascii') for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
    #We now have all chars in ABC in their byte form
    #now we need to XOR against each char
    db[hexx]=[''.join([chr((a^b)) for a,b in zip(hex_bytes,(char)*len(hexx))]) for char in charlist2]
    return db

def single_byte_XOR_final(hexush,x):
    #takes a hex and a char, turns them into bytes and returns their XOR in bytes after zipping them
    return ''.join([chr(x) for x in [a^b for a,b in zip([bytes(x,'ascii')[0]]*
                                                 len([byte for byte in bytes.fromhex(hexush)])
                                                 ,[byte for byte in bytes.fromhex(hexush)])]])

def check_occurences(decrypted_text):
    '''checked how many times a charater occured and retuns a percrntage list of them'''
    return[tuple([char,decrypted_text.count(char)/len(decrypted_text)*100]) for char in charlist2[:26]]

'''
                                            OLD FUNCTION
def check_score(list_of_counted_chars):
    sums all letter percenteages from the check_occurences function 
    return sum([list_of_counted_chars[i][1] for i in range(0,len(list_of_counted_chars))])
'''

def tups_to_dict(tups):
    #takes the output of check_occurences and returns a dictonary
    dictio={}
    #for tupset in tups:
    for tup in tups:
        dictio.update({tup[0].upper():tup[1]})
        
    return dictio

def dictionary_to_sorted_string(dictionary):
    #takes a dictionary and sorts it
    #Returns a sorted string
    return "".join(sorted(dictionary,key=dictionary.get,reverse=True)).upper()

def check_scores(sorted_text):
    #takes sorted text from dictionary_to_sorted_string and returns the score of the text based on the algorithm
    ETAOIN='ETAOINSHRDLCUMWFGYPBVKJXQZ'
    score=0
    #takes sorted text
    #gives you a score betweek 1-12 for each set
    for letter in sorted_text[-6:]:
        if letter in ETAOIN[-6:]:
            score+=1
    for letter in sorted_text[:6]:
        if letter in ETAOIN[:6]:
            score+=1
    return score
    

#Code:
def main():
    list_of_decrypted_texts=[single_byte_XOR_final(hexush,char) for char in charlist2]
    #[check_occurences(list_of_decrypted_texts) for item in list_of_decrypted_texts]
    list_of_letter_scores=[check_occurences(item) for item in list_of_decrypted_texts]

    #scores=[check_score(item) for item in list_of_letter_scores]
    #scores=[dictionary_to_sorted_string(tups_to_dict(tupset)) for tupset in list_of_letter_scores]
    scores=[dictionary_to_sorted_string(tups_to_dict(tupset)) for tupset in list_of_letter_scores]
    numscores=[check_scores(sorted_text) for sorted_text in scores]


    print(f'The encrypted hex text is \n:{hexush}\n')
    print(f'Decrypted text is: \n{list_of_decrypted_texts[numscores.index(max(numscores))]}')

if __name__ == '__main__':
    main()