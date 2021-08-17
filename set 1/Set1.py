import codecs
#2
hex = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
b64 = codecs.encode(codecs.decode(hex, 'hex'), 'base64').decode()
print(b64)


#--------------
#2
'''
#hex to int
he1='1c0111001f010100061a024b53535009181c'
he2='686974207468652062756c6c277320657965'
base=16
hti1=int(he1,base)
hti2=int(he2,base)
#int to bin
itb1=bin(hti1)
itb2=bin(hti2)
#convert to desired binary (removeing the 0b in the beginning)
resbin1=itb1[::2]
resbin2=itb2[::2]

#lengh the binaries so they have the same langh:
    # find the desired langh for both binaries
desired_length = len(resbin1) if len(resbin1) > len(resbin2) else len(resbin2)
    # use zfill to fill out zeros to the desired len
resbin1=resbin1.zfill(desired_length)
resbin2=resbin2.zfill(desired_length)

#XOR the binaries:
    #First we zip the two binaries
zippedbin=zip(resbin1,resbin2) #This generates tuples of each bit in the two binaries
    #itarate and XOR the bits:
XORl=[int(bit1)^ int(bit2) for bit1,bit2 in zip(resbin1,resbin2)]
    # outputs a list of the XOR which we then convert to string by joining each index of the list

XOR="".join([str(bits) for bits in XORl])
'''

he1='1c0111001f010100061a024b53535009181c'
he2='686974207468652062756c6c277320657965'
def xorhex(some_hex,compared_hex):
	inthex=bin(int(some_hex,16))[::2]
	feedhex=bin(int(feed,16))[::2]
	desired_length = len(inthex) if len(inthex) > len(feedhex) else len(feedhex)
	inthex=inthex.zfill(desired_length)
	feedhex=feedhex.zfill(desired_length)
	zipped=zip(inthex,feedhex)
	l=[int(bit1)^ int(bit2) for bit1,bit2 in zipped]
	xor= "".join([str(bits) for bits in l])
	xor_int=int(xor)
	return hex(xor)
xorhex(he1,he2)