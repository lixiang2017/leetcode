'''
AC
'''
def blackhole(n):
    while True:
        four = list(str(n))
        large = sorted(four, reverse=True)
        small = sorted(four)
        large = int(''.join(large))
        small = int(''.join(small))
        diff = large - small
        print('%04d - %04d = %04d' % (large, small, diff))
        if diff == 6174 or 0 == diff:
            break
        n = str(diff).zfill(4)


n = input().zfill(4)
blackhole(n)