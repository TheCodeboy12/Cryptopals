def fixed_XOR(hex1,comparedhex):
	'''
	First we get two hexes then we turn them to bytearrays .fromhex
	We check if their byte lengh is equal since we cant XOR them if they are not
	Then I basically zip the two byte arrays which turns them into tu
	'''
	assert len(bytearray.fromhex(hex1))==len(bytearray.fromhex(comparedhex)), "You must pass equal-length objects"
	return ''.join([bytes([a ^ b]).hex() for a, b in zip(bytearray.fromhex(hex1), bytearray.fromhex(comparedhex))])
