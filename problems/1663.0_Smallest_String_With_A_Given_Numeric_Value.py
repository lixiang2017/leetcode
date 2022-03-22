'''
T: O(1)
S: O(1)

Runtime: 51 ms, faster than 93.09% of Python3 online submissions for Smallest String With A Given Numeric Value.
Memory Usage: 14.8 MB, less than 94.47% of Python3 online submissions for Smallest String With A Given Numeric Value.
'''
class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        # based on 'a' * n, first
        # 'z' as many as possible
        z_cnt, r = divmod(k - n - 1, 25)
        a_cnt = n - z_cnt - 1
        return 'a' * a_cnt + chr(ord('a') + r + 1) + 'z' * z_cnt
