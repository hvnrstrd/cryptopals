ASCII_MAP = {chr(i): i for i in range(128)}

key = "ICE"
text = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"

key_bytes = [ASCII_MAP[c] for c in key]
text_bytes = [ASCII_MAP[c] for c in text]

def repeating_key_xor(text, key):
    result = []
    for i, byte in enumerate(text):
        result.append(byte ^ key[i % len(key)])
    return result

xor_result = repeating_key_xor(text_bytes, key_bytes)
HEX_CHARS = "0123456789abcdef"
def bytes_to_hex(data):
    result = ""
    for byte in data:
        result += HEX_CHARS[byte >> 4]
        result += HEX_CHARS[byte & 15]
    return result

print(bytes_to_hex(xor_result))