'''
Runtime: 104 ms, faster than 17.39% of Python3 online submissions for Integer to Roman.
Memory Usage: 13.9 MB, less than 80.25% of Python3 online submissions for Integer to Roman.
'''
class Solution:
    def intToRoman(self, num: int) -> str:
        value = [
            [1000, 'M'],
            [900,  'CM'],
            [500,  'D'],
            [400,  'CD'],
            [100,  'C'],
            [90,   'XC'],
            [50,   'L'],
            [40,   'XL'],
            [10,   'X'],
            [9,    'IX'],
            [5,    'V'],
            [4,    'IV'],
            [1,    'I'],
        ]
        ans = ''
        for v, s in value:
            cnt, num = divmod(num, v)
            ans += s * cnt
        return ans 



'''
Runtime: 111 ms, faster than 28.07% of Python3 online submissions for Integer to Roman.
Memory Usage: 14 MB, less than 35.57% of Python3 online submissions for Integer to Roman.
'''
class Solution:
    def intToRoman(self, num: int) -> str:
        symbol = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I'),
        ]
        seq = []
        for x, s in symbol:
            cnt, num = divmod(num, x)
            seq += [s] * cnt
        return ''.join(seq)
