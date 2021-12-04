
zero_cnt = [0] * 20
one_cnt = [0] * 20
max_len = 0
line_cnt = 0
with open('input') as f:
    for binary in f:
        if line_cnt in (5, 6, 7):
            print(f'===={binary}-----')
        # binary 前后或有空格！！！ 有换行符
        binary = binary.strip()
        line_cnt += 1
        max_len = max(max_len, len(binary))
        if max_len == 13:
            print(binary)
        for i, b in enumerate(binary):
            if b == '0':
                zero_cnt[i] += 1

zero_cnt = zero_cnt[: max_len]
one_cnt = [line_cnt - zero for zero in zero_cnt]
most = ['0' if zcnt > ocnt else '1' for zcnt, ocnt in zip(zero_cnt, one_cnt)]
least = ['1' if zcnt > ocnt else '0' for zcnt, ocnt in zip(zero_cnt, one_cnt)]
gamma = int(''.join(most), 2)
epsilon = int(''.join(least), 2)


print('zero_cnt: ', zero_cnt)
print('max_len: ', max_len)
print('line_cnt: ', line_cnt)
print('gamma: ', gamma, 'epsilon: ', epsilon, 'product: ', gamma * epsilon)

'''
====101001100000
-----
====110001010000
-----
====111110011011
-----
zero_cnt:  [494, 493, 506, 457, 523, 485, 481, 513, 480, 492, 522, 496]
max_len:  12
line_cnt:  1000
gamma:  3437 epsilon:  658 product:  2261546
'''

