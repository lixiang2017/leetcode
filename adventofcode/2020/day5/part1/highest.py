

highest = 0


def cal_seat_id(card):
    row = col = 0
    i = 0
    rs = 128
    while i < 7:
        bf = card[i]
        if bf == 'F':
            pass
        elif bf == 'B':
            row += (rs // 2)
        i += 1
        rs >>= 1
    # col
    i = 7
    cs = 8
    while i < 10:
        lr = card[i]
        if lr == 'L':
            pass
        elif lr == 'R':
            col += (cs // 2)
        i += 1
        cs >>= 1

    # print('row: ', row, 'col: ', col)
    return row * 8 + col


def main():
    global highest
    with open('input') as f:
        for line in f:
            line = line.strip()
            seat_id = cal_seat_id(line)
            highest = max(highest, seat_id)

def test():
    assert cal_seat_id('FBFBBFFRLR') == 357
    assert cal_seat_id('BFFFBBFRRR') == 567
    assert cal_seat_id('FFFBBBFRRR') == 119
    assert cal_seat_id('BBFFBBFRLL') == 820

def test2():
    main()
    global highest
    print('highest: ', highest)

test2()

'''
 pytest highest.py
=========================================================== test session starts ===========================================================
platform darwin -- Python 3.8.6, pytest-6.2.2, py-1.10.0, pluggy-0.13.1
rootdir: /Users/xiangli
plugins: hypothesis-6.1.1, xdist-2.2.1, timeout-1.4.2, forked-1.3.0
collected 2 items

highest.py ..                                                                                                                       [100%]

============================================================ 2 passed in 0.05s ============================================================
'''

'''
 python3 highest.py
highest:  883
'''


