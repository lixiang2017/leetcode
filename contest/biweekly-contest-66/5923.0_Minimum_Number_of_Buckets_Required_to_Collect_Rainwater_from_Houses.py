'''
207 / 207 个通过测试用例
状态：通过
执行用时: 88 ms
内存消耗: 16.2 MB
提交时间：1 天前
'''
class Solution:
    def minimumBuckets(self, street: str) -> int:
        if 'HHH' in street:
            return -1
        if street == 'H':
            return -1
        if len(street) >= 2 and (street[: 2] == 'HH' or street[-2:] == 'HH'):
            return -1
        
        N = len(street)
        st = list(street)
        ans = 0
        i = 0
        while i + 2 < N:
            if st[i] == 'H' and st[i+1] == '.' and st[i+2] == 'H':
                ans += 1
                st[i] = '.'
                st[i+2] = '.'
                i += 3
            else:
                i += 1
        
        ans += Counter(st)['H']
        return ans
    

