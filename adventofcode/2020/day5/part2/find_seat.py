

highest = 0
all_seat = set()

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


def test():
    assert cal_seat_id('FBFBBFFRLR') == 357
    assert cal_seat_id('BFFFBBFRRR') == 567
    assert cal_seat_id('FFFBBBFRRR') == 119
    assert cal_seat_id('BBFFBBFRLL') == 820


with open('input') as f:
    for line in f:
        line = line.strip()
        seat_id = cal_seat_id(line)
        all_seat.add(seat_id)
        highest = max(highest, seat_id)


for s in range(1, highest + 1):
    if s - 1 in all_seat and s + 1 in all_seat and s not in all_seat:
        print('seat_id found: ', s)

'''
seat_id found:  532
'''




