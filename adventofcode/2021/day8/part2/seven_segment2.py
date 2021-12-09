'''
wrong
'''

'''
0   abcefg  6
1   cf      2   -
2   acdeg   5  
3   acdfg   5
4   bcdf    4   -
5   abdfg   5
6   abdefg  6
7   acf     3   -
8   abcdefg 7   -
9   abcefg  6



acedgfb: 8
cdfbe: 5
gcdfa: 2
fbcad: 3
dab: 7
cefabd: 9
cdfgeb: 6
eafb: 4
cagedb: 0
ab: 1

'''

memo = {
    "acedgfb": "8",
    "cdfbe": "5",
    "gcdfa": "2",
    "fbcad": "3",
    "dab": "7",
    "cefabd": "9",
    "cdfgeb": "6",
    "eafb": "4",
    "cagedb": "0",
    "ab": "1",
}

memo2 = {}
for k, v in memo.items():
    k = ''.join(sorted(list(k)))
    memo2[k] = v 

print(memo2)

def count1478(file_name):
    _sum = 0
    with open(file_name) as f:
        for line in f:
            segs = line.strip().split('|')[1].strip().split(' ')
            x = 0
            for seg in segs:
                seg = seg.strip()
                seg = ''.join(sorted(list(seg)))
                x = x * 10 + int(memo2[seg])
            print('x: ', x)
            _sum += x               

    print('_sum: ', _sum)
    return _sum


c = count1478('input')

