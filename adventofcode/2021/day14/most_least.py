

from collections import defaultdict, Counter

def get_diff(file_name, round):
    print('=============')
    template = ''
    # tuple pair -> char
    rules = defaultdict(str)
    with open(file_name) as f:
        for line in f:
            line = line.strip()
            if line == '':
                continue
            if '->' in line:
                left, right = map(str.strip, line.split('->'))
                if (left[0], left[1]) in rules:
                    print('exist: ', (left[0], left[1]), rules[(left[0], left[1])])
                rules[(left[0], left[1])] = right
            else:
                template = line 

    n = len(template)
    init = defaultdict(int)
    for i in range(n - 1):
        init[(template[i], template[i + 1])] += 1   ### !!!!!

    # print('rules: ', rules)
    for _ in range(round):
        now = defaultdict(int)
        for pair in init:
            l1, l2 = pair
            c = init[(l1, l2)]
            if (l1, l2) in rules:
                r = rules[(l1, l2)]
                now[(l1, r)] += c 
                now[(r, l2)] += c 
            else:
                #!!!
                print('not in rules')
                now[(l1, l2)] = c 
        init = now 

    # get len
    now_len = 1 
    C = Counter([template[-1]])  # tailing one
    for pair, cnt in init.items():
        # only count left  #right
        l, r = pair
        now_len += cnt
        C[l] += cnt 
    print('round, now_len:', round, now_len)
    print('C: ', C)
    print(C['B'], C['C'], C['H'], C['N'])

    low, high =  float('inf'), 0 
    for ch, cnt in C.items():
        low = min(low, cnt)
        high = max(high, cnt)
    print('low, high, diff: ', low, high, high - low)


c1 = get_diff('input1', 5)
c2 = get_diff('input1', 10)
c = get_diff('input', 10)

c12 = get_diff('input1', 40)
c22 = get_diff('input', 40)
'''
=============
round, now_len: 5 97
C:  Counter({'B': 46, 'N': 23, 'C': 15, 'H': 13})
46 15 13 23
low, high, diff:  13 46 33
=============
round, now_len: 10 3073
C:  Counter({'B': 1749, 'N': 865, 'C': 298, 'H': 161})
1749 298 161 865
low, high, diff:  161 1749 1588
=============
round, now_len: 10 19457
C:  Counter({'H': 3978, 'V': 3056, 'F': 2711, 'P': 2643, 'N': 2082, 'B': 1490, 'K': 1378, 'C': 972, 'S': 577, 'O': 570})
1490 972 3978 2082
low, high, diff:  570 3978 3408
=============
round, now_len: 40 3298534883329
C:  Counter({'B': 2192039569602, 'N': 1096047802353, 'C': 6597635301, 'H': 3849876073})
2192039569602 6597635301 3849876073 1096047802353
low, high, diff:  3849876073 2192039569602 2188189693529
=============
round, now_len: 40 20890720927745
C:  Counter({'H': 4290332671591, 'V': 3622697825643, 'F': 3054025187575, 'P': 2770033357678, 'N': 1785757384819, 'B': 1728846105420, 'K': 1609430580936, 'C': 816071429248, 'S': 647537090186, 'O': 565989294649})
1728846105420 816071429248 4290332671591 1785757384819
low, high, diff:  565989294649 4290332671591 3724343376942

'''

