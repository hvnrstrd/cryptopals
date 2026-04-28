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
    result = []
    for byte in data:
        result.append(byte ^ key)
    return result

ENGLISH_FREQ = "etaoinshrdlu "

def score(message):
    score = 0
    for byte in message:
        if chr(byte) in ENGLISH_FREQ:  # chr() переводит байт в символ
            score += 1
    return score

hex_str = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
data = hex_to_bytes(hex_str)

best_score = 0
best_key = 0
best_msg = []

for key in range(256):
    decrypted = single_byte_xor(data, key)
    s = score(decrypted)
    if s > best_score:
        best_score = s
        best_key = key
        best_msg = decrypted

print("key:", best_key)
print("text:", "".join(chr(b) for b in best_msg))