'''
执行用时：44 ms, 在所有 Python3 提交中击败了79.19% 的用户
内存消耗：15.3 MB, 在所有 Python3 提交中击败了33.53% 的用户
通过测试用例：24 / 24
'''
class Solution:
    def originalDigits(self, s: str) -> str:
        d = {
            0: 'zero',
            1: 'one',
            2: 'two',
            3: 'three',
            4: 'four',
            5: 'five',
            6: 'six',
            7: 'seven',
            8: 'eight',
            9: 'nine',
        }
        ans = [0] * 10
        c = Counter(s)
        
        # process sequence
        seq = [('z', 0), ('w', 2), ('u', 4), ('x', 6), ('g', 8),
                ('s', 7), ('f', 5), ('h', 3), ('i', 9), ('o', 1)]

        def process(specical_ch, digit):
            if specical_ch in c:
                find_cnt = c[specical_ch]
                ans[digit] += find_cnt
                for ch in d[digit]:
                    c[ch] -= find_cnt
                    if c[ch] == 0:
                        c.pop(ch) 

        for ch, digit in seq:
            process(ch, digit)

        return ''.join([str(i) * cnt for i, cnt in enumerate(ans)])



