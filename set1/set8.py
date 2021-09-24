from set6 import sort_dict
def break_to_chunks(b64decoded:bytes,biggest):
    '''
    Takes the decoded b64 text and breaks it into byte sizes between 2-42 as suggested]
    '''
    data={}
    # data looks like this : {bytesize:chunks of the b64 decoded text}
    for bytesize in range(2,biggest):
        chunks=[b64decoded[i:i+bytesize] for i in range(0,len(b64decoded),bytesize)]
        reps= len(chunks)-len(set(chunks))
        data.update({bytesize:reps})
    return max(set(data.values()))

def main():
    d=[bytes.fromhex(x) for x in open('8.txt').readlines()]
    size=16
    yea=[]
    for t in d:
        yea.append(break_to_chunks(t, size))
    
    print(f'The cipher that is encrypted is: {d[yea.index(max(yea))]}')

if __name__ == '__main__':
    main()