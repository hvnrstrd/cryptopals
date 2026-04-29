import os

HEX_MAP = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'a':10,'b':11,'c':12,'d':13,'e':14,'f':15}

def hex_to_bytes(hex_str):
    result = []
    for i in range(0, len(hex_str), 2):
        high = HEX_MAP[hex_str[i]]
        low = HEX_MAP[hex_str[i+1]]
        result.append((high << 4) | low)
    return result

def count_duplicate_blocks(data, block_size=16):
    blocks = []
    for i in range(0, len(data), block_size):
        blocks.append(tuple(data[i:i+block_size]))
    return len(blocks) - len(set(blocks))

script_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(script_dir, 'data', '8.txt')

f = open(data_path, 'r')
lines = [line.strip() for line in f]
f.close()

best_line = ""
best_line_num = 0
best_duplicates = 0

for i, line in enumerate(lines):
    data = hex_to_bytes(line)
    duplicates = count_duplicate_blocks(data)
    if duplicates > best_duplicates:
        best_duplicates = duplicates
        best_line = line
        best_line_num = i

print("line number:", best_line_num)
print("duplicates:", best_duplicates)
print("hex:", best_line[:64], "...")