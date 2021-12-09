

'''         len
0   abcefg  6
1   cf      2   -
2   acdeg   5  
3   acdfg   5
4   bcdf    4   -
5   abdfg   5
6   abdefg  6
7   acf     3   -
8   abcdefg 7   -
9   abcdfg  6


len  2   3   4       5 5 5               6 6 6                       7
x    1   7   4        2     3    5       [0]     6    [9]             8
    cf acf  bcdf   acdeg/acdfg/abdfg   abcefg/abdefg/abcdfg        abcdefg
                                          d     c     e

               对应数字
长度为2的字符  -> 1
长度为3的字符  -> 7
长度为4的字符  -> 4
长度为7的字符  -> 8

（公有的a字符无法区分，只能用 b d了）
长度为2、3、4的字符 公用c f字符 -> 长度为5的有这两个公用字符c f的对应数字是3
长度为4的字符比长度为2的字符多了b d两个字符 -> 长度为5的字符串都有b d这两个的对应数字是5


长度为2、3、4的字符 公用c f字符 -> 长度为6的只有一个公用字符 f的对应数字是6,其他两个都有两个公用字符
# 0 VS 9
0  ab ce fg
6  ab de fg
9  ab cd fg
突破
3 : acdfg 全部有这五个字符的 长度为6的是9
另一个是0 
'''

from itertools import chain

def get_sum(file_name):
    _sum = 0
    with open(file_name) as f:
        seen = set()
        # str -> digit
        str2digit = {}
        digit2str = {}

        for line in f:
            segs0 = line.strip().split('|')[0].strip().split(' ')
            segs = line.strip().split('|')[1].strip().split(' ')
            
            seen.clear()
            str2digit.clear()
            digit2str.clear()
            for seg in chain(segs0, segs):
            # for seg in segs0:
                seg = seg.strip()
                seg = ''.join(sorted(list(seg)))
                seen.add(seg)

            # len 5 6
            l5, l6 = set(), set()
            for s in seen:
                if len(s) == 2:
                    str2digit[s] = 1
                    digit2str[1] = s 
                elif len(s) == 3:
                    str2digit[s] = 7
                    digit2str[7] = s 
                elif len(s) == 4:
                    str2digit[s] = 4
                    digit2str[4] = s 
                elif len(s) == 7:
                    str2digit[s] = 8
                    digit2str[8] = s
                elif len(s) == 5:
                    l5.add(s)
                elif len(s) == 6:
                    l6.add(s)

            # to get 对应数字是3
            s53 = [s5 for s5 in l5 if digit2str[1][0] in s5 and digit2str[1][1] in s5][0]
            str2digit[s53] = 3
            digit2str[3] = s53
            # to get 对应数字是6
            s66 = [s6 for s6 in l6 if digit2str[1][0] not in s6 or digit2str[1][1] not in s6][0]
            str2digit[s66] = 6
            digit2str[6] = s66
            # to get bd
            bd = list(set(digit2str[4]) - set(digit2str[1]))
            # to get 5
            s55 = [s5 for s5 in l5 if bd[0] in s5 and bd[1] in s5][0]
            str2digit[s55] = 5
            digit2str[5] = s55     
            # to get left l5, 2
            s52 = [s5 for s5 in l5 if s5 not in str2digit][0]
            str2digit[s52] = 2
            digit2str[2] = s52

            # to get 9
            s69 = [s6 for s6 in l6 if all(ch in s6 for ch in digit2str[3])][0]
            str2digit[s69] = 9
            digit2str[9] = s69  
            # to get left s6,  0
            s60 = [s6 for s6 in l6 if s6 not in str2digit][0]
            str2digit[s60] = 0
            digit2str[0] = s60

            # calculate x
            x = 0
            for seg in segs:
                seg = ''.join(sorted(list(seg)))
                x = x * 10 + str2digit[seg]
            _sum += x               

    print('_sum: ', _sum)
    return _sum


s1 = get_sum('input1')
s2 = get_sum('input2')
s = get_sum('input')

'''
_sum:  5353
_sum:  61229
_sum:  1011785
'''

