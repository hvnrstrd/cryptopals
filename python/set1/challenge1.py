HEX_MAP = {
    '0': 0,  '1': 1,  '2': 2,  '3': 3,
    '4': 4,  '5': 5,  '6': 6,  '7': 7,
    '8': 8,  '9': 9,  'a': 10, 'b': 11,
    'c': 12, 'd': 13, 'e': 14, 'f': 15
}

B64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def hex_to_bytes(hex_str):
    result = []
    for i in range(0, len(hex_str), 2):
        high = HEX_MAP[hex_str[i]]
        low  = HEX_MAP[hex_str[i+1]]
        result.append((high << 4) | low)
    return result

def bytes_to_base64(data):
    result = ""
    for i in range(0, len(data), 3):
        a = data[i]
        b = data[i+1] if i+1 < len(data) else 0
        c = data[i+2] if i+2 < len(data) else 0

        result += B64[a >> 2]
        result += B64[((a & 3) << 4) | (b >> 4)]
        result += B64[((b & 15) << 2) | (c >> 6)]
        result += B64[c & 63]
    return result

hex_str = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
print(bytes_to_base64(hex_to_bytes(hex_str)))