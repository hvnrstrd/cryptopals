HEX_MAP = {
    '0': 0,  '1': 1,  '2': 2,  '3': 3,
    '4': 4,  '5': 5,  '6': 6,  '7': 7,
    '8': 8,  '9': 9,  'a': 10, 'b': 11,
    'c': 12, 'd': 13, 'e': 14, 'f': 15
}

def hex_to_bytes(hex_str):
    result = []
    for i in range(0, len(hex_str), 2):
        high = HEX_MAP[hex_str[i]]
        low  = HEX_MAP[hex_str[i+1]]
        result.append((high << 4) | low)
    return result

def xor_buffers(hex1, hex2):
    bytes1 = hex_to_bytes(hex1)
    bytes2 = hex_to_bytes(hex2)
    result = []
    for i in range(len(bytes1)):
        result.append(bytes1[i] ^ bytes2[i])
    return result

HEX_CHARS = "0123456789abcdef"

def bytes_to_hex(data):
    result = ""
    for byte in data:
        result += HEX_CHARS[byte >> 4]
        result += HEX_CHARS[byte & 15]
    return result

hex1 = "1c0111001f010100061a024b53535009181c"
hex2 = "686974207468652062756c6c277320657965"

print(bytes_to_hex(xor_buffers(hex1, hex2)))