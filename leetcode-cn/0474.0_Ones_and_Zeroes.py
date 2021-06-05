'''
approach: Hash Set + DP

执行用时：652 ms, 在所有 Python 提交中击败了99.69% 的用户
内存消耗：17.1 MB, 在所有 Python 提交中击败了31.19% 的用户
ref:
https://leetcode-cn.com/problems/ones-and-zeroes/solution/pythonjian-dan-yi-dong-de-jie-fa-by-semi-9fu3/
'''

class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        choices = {(0, 0, 0)} # (0s, 1s, length of set)
        contains = [(oneStr.count('0'), oneStr.count('1')) for oneStr in strs]
        for zero, one in contains:
            choices |= {(zero + z, one + o, cnt + 1) for z, o, cnt in choices \
                if zero + z <= m and one + o <= n}
        return max(cnt for _, _, cnt in choices)



'''
DFS

20 / 70 个通过测试用例
状态：超出时间限制
提交时间：1 分钟内
最后执行的输入：
["0","11","1000","01","0","101","1","1","1","0","0","0","0","1","0","0110101","0","11","01","00","01111","0011","1","1000","0","11101","1","0","10","0111"]
9
80
'''

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        self.maximum = 0
        N = len(strs)
        # (strs, cur_size, next_index_to_process, N, left_zeros, left_ones)
        def dfs(strs, cur, i, N, m, n):
            if m < 0 or n < 0:
                return
            self.maximum = max(self.maximum, cur)

            if i >= N:
                return
            zeros = strs[i].count('0')
            ones = len(strs[i]) - zeros
            # not choose
            dfs(strs, cur, i + 1, N, m, n)
            # choose
            dfs(strs, cur + 1, i + 1, N, m - zeros, n - ones)

        dfs(strs, 0, 0, N, m, n)
        return self.maximum





'''
DFS + @lru_cache(None)

执行用时：2976 ms, 在所有 Python3 提交中击败了81.15% 的用户
内存消耗：391.3 MB, 在所有 Python3 提交中击败了5.15% 的用户
'''

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        self.maximum = 0
        N = len(strs)
        # (strs, cur_size, next_index_to_process, N, left_zeros, left_ones)
        @lru_cache(None)
        def dfs(cur, i, N, m, n):
            if m < 0 or n < 0:
                return
            self.maximum = max(self.maximum, cur)

            if i >= N:
                return
            zeros = strs[i].count('0')
            ones = len(strs[i]) - zeros
            # not choose
            dfs(cur, i + 1, N, m, n)
            # choose
            dfs(cur + 1, i + 1, N, m - zeros, n - ones)

        dfs(0, 0, N, m, n)
        return self.maximum


'''
DFS + @lru_cache(None) + nonlocal
执行用时：2740 ms, 在所有 Python3 提交中击败了94.92% 的用户
内存消耗：391.3 MB, 在所有 Python3 提交中击败了5.15% 的用户
'''

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        maximum = 0
        N = len(strs)
        # (strs, cur_size, next_idex_to_process, N, left_zeros, left_ones)
        @lru_cache(None)
        def dfs(cur, i, N, m, n):
            if m < 0 or n < 0:
                return
            nonlocal maximum
            maximum = max(maximum, cur)

            if i >= N:
                return
            zeros = strs[i].count('0')
            ones = len(strs[i]) - zeros
            # not choose
            dfs(cur, i + 1, N, m, n)
            # choose
            dfs(cur + 1, i + 1, N, m - zeros, n - ones)

        dfs(0, 0, N, m, n)
        return maximum
