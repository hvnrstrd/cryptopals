HEX_CHARS = "0123456789abcdef"
B64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
B64_MAP = {}
for i in range(64):
    B64_MAP[B64[i]] = i

CHAR_TO_NUM = {}
NUM_TO_CHAR = {}
ALL_CHARS = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~\n\r\t"
for c in ALL_CHARS:
    n = 0
    if c == '\t': n = 9
    elif c == '\n': n = 10
    elif c == '\r': n = 13
    else:
        offset = 32
        idx = ALL_CHARS.index(c)
        if idx < 95:
            n = 32 + idx
    CHAR_TO_NUM[c] = n
    NUM_TO_CHAR[n] = c

ENGLISH_FREQ_BYTES = set()
for c in "etaoinshrdlu ":
    ENGLISH_FREQ_BYTES.add(CHAR_TO_NUM[c])

def base64_to_bytes(data):
    result = []
    for i in range(0, len(data), 4):
        a = B64_MAP.get(data[i], 0)
        b = B64_MAP.get(data[i+1], 0) if i+1 < len(data) else 0
        c = B64_MAP.get(data[i+2], 0) if i+2 < len(data) else 0
        d = B64_MAP.get(data[i+3], 0) if i+3 < len(data) else 0
        result.append((a << 2) | (b >> 4))
        if i+2 < len(data) and data[i+2] != '=':
            result.append(((b & 15) << 4) | (c >> 2))
        if i+3 < len(data) and data[i+3] != '=':
            result.append(((c & 3) << 6) | d)
    return result

def count_bits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

def hamming_distance(bytes1, bytes2):
    distance = 0
    for i in range(len(bytes1)):
        distance += count_bits(bytes1[i] ^ bytes2[i])
    return distance

def single_byte_xor(data, key):
    result = []
    for byte in data:
        result.append(byte ^ key)
    return result

def score(message):
    s = 0
    for byte in message:
        if byte in ENGLISH_FREQ_BYTES:
            s += 1
    return s

def find_best_key_byte(block):
    best_score = 0
    best_key = 0
    for key in range(256):
        decrypted = single_byte_xor(block, key)
        s = score(decrypted)
        if s > best_score:
            best_score = s
            best_key = key
    return best_key

f = open('..python\\set1\\data\\6.txt', 'r')
content = ""
for line in f:
    content += line.replace('\n', '')
f.close()

data = base64_to_bytes(content)

best_keysize = 0
best_distance = 999999.0

for keysize in range(2, 41):
    num_blocks = len(data) // keysize
    if num_blocks < 4:
        continue
    
    total = 0.0
    count = 0
    for j in range(num_blocks - 1):
        for k in range(j + 1, num_blocks):
            b1 = data[j*keysize:(j+1)*keysize]
            b2 = data[k*keysize:(k+1)*keysize]
            total += hamming_distance(b1, b2) / keysize
            count += 1
            if count >= 50:
                break
        if count >= 50:
            break
    
    avg = total / count
    if avg < best_distance:
        best_distance = avg
        best_keysize = keysize

print("keysize:", best_keysize)

key = []
for i in range(best_keysize):
    block = []
    j = i
    while j < len(data):
        block.append(data[j])
        j += best_keysize
    key.append(find_best_key_byte(block))

key_text = ""
for k in key:
    if k in NUM_TO_CHAR:
        key_text += NUM_TO_CHAR[k]
    else:
        key_text += "?"
print("key:", key_text)

decrypted = []
for i in range(len(data)):
    decrypted.append(data[i] ^ key[i % best_keysize])

result = ""
for b in decrypted:
    if b in NUM_TO_CHAR:
        result += NUM_TO_CHAR[b]
print("text:")
print(result[:300])