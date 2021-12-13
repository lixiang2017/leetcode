


def get_row_col(file_name):
    row = col = 0
    with open(file_name) as f:
        for line in f:
            line = line.strip()
            if line == '':
                break
            x, y = map(int, line.split(','))
            col = max(col, x)
            row = max(row, y)
    col += 1
    row += 1    
    return row, col 


def visible_cnt(file_name):
    print('=================')
    row, col = get_row_col(file_name)
    folds = []
    print('row, col: ', row,col)
    grid = [[None] * col for _ in range(row)]

    with open(file_name) as f:
        for line in f:
            line = line.strip()
            if line == '':
                continue
            if 'fold' not in line:
                x, y = map(int, line.split(','))
                grid[y][x] = '#'
            elif 'fold' in line:
                line = line.replace('fold along ', '').strip()
                xy, num = line.split('=')
                num = int(num)
                folds.append((xy, num))

    fold_cnt = 0
    now_row, now_col = row, col 
    for xy, num in folds:
        # just fold once
        #if fold_cnt == 1:
        #    break
        if xy == 'x':
            # 0..x-1  x  x+1..col
            for i in range(now_row):
                for j in range(num):
                    grid[i][j] = (grid[i][j] or grid[i][now_col - 1 - j])

            now_col = num
        elif xy == 'y':
            # 0..y-1  y  y+1..row
            for i in range(num):
                for j in range(now_col):
                    grid[i][j] = (grid[i][j] or grid[now_row - 1 - i][j])

            now_row = num 
        fold_cnt += 1

        cnt = 0
        for i in range(now_row):
            for j in range(now_col):
                if grid[i][j] == '#':
                    cnt += 1
        print('cnt: ', cnt)
        print('now_row, now_col: ', now_row, now_col)
        print('----------------')
    
    xth = 0
    for i in range(now_row):
        for j in range(now_col):
            #if xth % 5 == 0:
            #    print('\n', end=' ')
            if grid[i][j] == '#':
                print('#', end='')
            else:
                print('.', end='')
            xth += 1
        print('\n', end='')
    return cnt 


c1 = visible_cnt('input1')
c = visible_cnt('input')

'''
fold once
row, col:  15 11
cnt:  17
row, col:  895 1311
cnt:  671
'''

'''
fold all
row, col:  15 11
cnt:  16
row, col:  895 1311
cnt:  97
'''

'''
=================
row, col:  15 11
cnt:  17
cnt:  16
=================
row, col:  895 1311
cnt:  671
cnt:  545
cnt:  461
cnt:  383
cnt:  328
cnt:  278
cnt:  228
cnt:  193
cnt:  165
cnt:  138
cnt:  120
cnt:  97

# # # . . . # # . . # # # . . # . . # . . # # . . # # # . . # . . # . # . . . .
# . . # . # . . # . # . . # . # . . # . # . . # . # . . # . # . # . . # . . . .
# . . # . # . . . . # . . # . # # # # . # . . # . # . . # . # # . . . # . . . .
# # # . . # . . . . # # # . . # . . # . # # # # . # # # . . # . # . . # . . . .
# . . . . # . . # . # . . . . # . . # . # . . # . # . # . . # . # . . # . . . .
# . . . . . # # . . # . . . . # . . # . # . . # . # . . # . # . . # . # # # # .

'''



'''
python3 day13.py
671
1 1 1 0 0 0 1 1 0 0 1 1 1 0 0 1 0 0 1 0 0 1 1 0 0 1 1 1 0 0 1 0 0 1 0 1 0 0 0 0
1 0 0 1 0 1 0 0 1 0 1 0 0 1 0 1 0 0 1 0 1 0 0 1 0 1 0 0 1 0 1 0 1 0 0 1 0 0 0 0
1 0 0 1 0 1 0 0 0 0 1 0 0 1 0 1 1 1 1 0 1 0 0 1 0 1 0 0 1 0 1 1 0 0 0 1 0 0 0 0
1 1 1 0 0 1 0 0 0 0 1 1 1 0 0 1 0 0 1 0 1 1 1 1 0 1 1 1 0 0 1 0 1 0 0 1 0 0 0 0
1 0 0 0 0 1 0 0 1 0 1 0 0 0 0 1 0 0 1 0 1 0 0 1 0 1 0 1 0 0 1 0 1 0 0 1 0 0 0 0
1 0 0 0 0 0 1 1 0 0 1 0 0 0 0 1 0 0 1 0 1 0 0 1 0 1 0 0 1 0 1 0 0 1 0 1 1 1 1 0

PCPHARKL
'''

