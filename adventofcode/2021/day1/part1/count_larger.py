
pre_num = 0
lineno = 0
larger_cnt = 0
with open('input') as f:
    for num in f:

        num = int(num)
        if num > pre_num and lineno > 0:
            larger_cnt += 1
        lineno += 1
        pre_num = num

print('larger_cnt: ', larger_cnt)

'''
python3 count_larger.py
larger_cnt:  1184
'''