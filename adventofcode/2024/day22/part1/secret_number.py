from pathlib import Path
import os

ans = 0
file_path = os.path.join(os.path.dirname(__file__), 'input')
lines = Path(file_path).read_text(encoding="utf-8")

lines = lines.split("\n")


MOD = 16777216

def generate_secret_number(x):
    x = (x << 6) ^ x
    x %= MOD
    
    x = (x >> 5) ^ x
    x %= MOD

    x = (x << 11) ^ x
    x %= MOD
    return x

# input1
# for line in lines:
#     x = int(line.strip())
#     for _ in range(10):
#         x = generate_secret_number(x)
#         print(x)
'''
15887950
16495136
527345
704524
1553684
12683156
11100544
12249484
7753432
5908254
'''

# input2
# total = 0
# for line in lines:
#     x = int(line.strip())
#     start_x = x
#     for _ in range(2000):
#         x = generate_secret_number(x)
#     total += x 
#     print(f"{start_x}: {x}")
# print("total:", total)
'''
1: 8685429
10: 4700978
100: 15273692
2024: 8667524
total: 37327623
'''

total = 0
for line in lines:
    x = int(line.strip())
    start_x = x
    for _ in range(2000):
        x = generate_secret_number(x)
    total += x 
    # print(f"{start_x}: {x}")
print("total:", total)
# total: 17262627539