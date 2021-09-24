import pdb
ct = bytes.fromhex('7b5a4215415d544115415d5015455447414c155c46155f4058455c5b523f')
def single_char_xor(input_bytes, char_value):
    """Returns the result of each byte being XOR'd with a single value.
    """
    output_bytes = b''
    for byte in input_bytes:
        output_bytes += bytes([byte ^ char_value])
        pdb.set_trace
    return output_bytes

for i in range(0,256):
    print(single_char_xor(ct, i),i)