
from pprint import pprint
from collections import Counter, defaultdict
from itertools import chain

nums = []
boards = []

n_idx = 0
# board
last_win_board_idx = 0
have_win_board = set()

with open('input') as f:
    nums = list(map(int, f.readline().strip().split(',')))
    while True:
        white_line = f.readline()
        board = []
        row = None
        for _ in range(5):
            row = list(map(int, f.readline().strip().split()))
            board.append(row)
        if not row:
            break
        boards.append(board)


# print(nums)
# pprint(boards)

BL = len(boards)
N = len(nums)
# all elements for every board, postion, element value -> idx (row * 5 + col)
pos = [defaultdict(int) for i in range(BL)]

# seen index in every board
seen = [set() for _ in range(BL)]

for i, b in enumerate(boards):
    for row_idx, row in enumerate(b):
        # element
        for col_idx, e in enumerate(row):
            pos[i][e] = row_idx * 5 + col_idx

def check(seen_indice):
    xys = [divmod(seen_idx, 5) for seen_idx in seen_indice]
    xs = [x for x, y in xys]
    ys = [y for x, y in xys]
    cx, cy = Counter(xs), Counter(ys)
    return max(cx.values()) == 5 or max(cy.values()) == 5

# round to find win_idx
Found = False
for i, x in enumerate(nums):
    # check every board
    for bi, b in enumerate(boards):
        if bi in have_win_board:
            continue
        if x in pos[bi]:
            seen[bi].add(pos[bi][x])
            # check seen[bi]
            if check(seen[bi]):
                have_win_board.add(bi)
                if len(have_win_board) == N:
                    n_idx = i 
                    last_win_board_idx = bi
                    Found = True
                    break
    if Found:
        break

seen_nums_sum = 0
for seen_idx in seen[last_win_board_idx]:
    x, y = divmod(seen_idx, 5)
    seen_nums_sum += boards[last_win_board_idx][x][y]

print('n: ', n_idx, 'last_win_board_idx: ', last_win_board_idx)
print('score: ', (sum(chain(*boards[last_win_board_idx])) - seen_nums_sum) * nums[n_idx])


'''
n:  80 last_win_board_idx:  84
score:  15561
'''

