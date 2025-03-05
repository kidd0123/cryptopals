from base64 import b16decode, b64encode
def hex_to_b64(hexbytes: bytes) -> bytes:
    return b64encode(b16decode(hexbytes, casefold=True))

if __name__ == "__main__":
    inp_as_str = b"49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    print(f"{inp_as_str=}")
    output = hex_to_b64(inp_as_str)
    expected_output = b"SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
    print(f"{output=}")
    if output==expected_output:
        print("Everything is working as expected")
    else:
        exit("Fatal Error check your code")

