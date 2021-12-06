


from collections import Counter

def get_cnt(file_name, day):
    dp = Counter()
    with open(file_name) as f:
        for line in f:
            inits = list(map(int, line.strip().split(',') ))
            dp = Counter(inits)

    for _ in range(day):
        next_dp = Counter()
        for timer in range(1, 9):
            if timer in dp:
                next_dp[timer - 1] = dp[timer]
        if 0 in dp:
            next_dp[6] += dp[0]
            next_dp[8] += dp[0]
        dp = next_dp

    cnt = sum(dp.values())
    print('day: ',day, 'cnt: ', cnt)
    return cnt



c1 = get_cnt('input1', 18)
c2 = get_cnt('input1', 80)
c3 = get_cnt('input1', 256)

c = get_cnt('input', 80)
c = get_cnt('input', 256)

'''
day:  18 cnt:  26
day:  80 cnt:  5934
day:  256 cnt:  26984457539
day:  80 cnt:  388739
day:  256 cnt:  1741362314973
'''