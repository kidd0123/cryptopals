from base64 import b16decode
def fixed_xor(inp1: bytes, inp2: bytes) -> bytes:
    if len(inp1) == len(inp2):
        return bytes(hex((int(inp1, 16) ^ int(inp2, 16)))[2:], 'utf-8')
    else:
        raise ValueError("inp strings are not equal!")


if __name__ == "__main__":
    inp = b"1c0111001f010100061a024b53535009181c"
    hex_str_to_xor_against = b"686974207468652062756c6c277320657965"
    expected_output = b"746865206b696420646f6e277420706c6179"
    output = fixed_xor(inp, hex_str_to_xor_against)
    if output == expected_output:
        print ("Success")
    else:
        print (f"{output=}")
        print (f"{expected_output=}")
        exit("Fatal Error!!")