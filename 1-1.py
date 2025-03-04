from base64 import b16decode, b64encode


def hex_to_b64(data_hex: bytes) -> bytes:
    return b64encode(b16decode(data_hex, casefold=True))

if __name__ == "__main__":
    inp_as_str = b"49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    output = hex_to_b64(inp_as_str)
    print(f"{inp_as_str=}")
    print(f"{output=}")
    expected_out = b"SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t" 
    if (output == expected_out):
        print ("Working as expected!!")
    else:
        exit("Error occured! Exiting")