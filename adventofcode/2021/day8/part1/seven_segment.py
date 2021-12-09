

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
'''


def count1478(file_name):
    c = 0
    with open(file_name) as f:
        for line in f:
            segs = line.strip().split('|')[1].strip().split(' ')
            for seg in segs:
                seg = seg.strip()
                if len(seg) in (2, 3, 4, 7):
                    c += 1
    print('c: ', c)
    return c 


c = count1478('input')

'''
c:  390
'''