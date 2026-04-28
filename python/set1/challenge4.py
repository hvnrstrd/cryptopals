HEX_MAP = {
    '0': 0, '1': 1, '2': 2, '3': 3,
    '4': 4, '5': 5, '6': 6, '7': 7,
    '8': 8, '9': 9, 'a': 10, 'b': 11,
    'c': 12, 'd': 13, 'e': 14, 'f': 15
}

def hex_to_bytes(hex_str):
    result = []
    for i in range(0, len(hex_str), 2):
        high = HEX_MAP[hex_str[i]]
        low  = HEX_MAP[hex_str[i+1]]
        result.append((high << 4) | low)
    return result

def single_byte_xor(data, key):
    return [byte ^ key for byte in data]

ENGLISH_FREQ = "etaoinshrdlu "

def score(message):
    s = 0
    for byte in message:
        if chr(byte) in ENGLISH_FREQ:
            s += 1
    return s

f = open('C:\\Users\\Asus\\cryptopals\\python\\set1\\bin\\4.txt', 'r')
lines = [line.strip() for line in f]
f.close()

best_score = 0
best_msg = []

for line in lines:           
    data = hex_to_bytes(line)
    for key in range(256):   
        decrypted = single_byte_xor(data, key)
        s = score(decrypted)
        if s > best_score:
            best_score = s
            best_msg = decrypted

print("text:", "".join(chr(b) for b in best_msg))