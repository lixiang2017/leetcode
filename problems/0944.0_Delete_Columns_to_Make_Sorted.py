'''
Runtime: 280 ms, faster than 55.79% of Python3 online submissions for Delete Columns to Make Sorted.
Memory Usage: 15.3 MB, less than 6.95% of Python3 online submissions for Delete Columns to Make Sorted.
'''
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ans = 0
        for t in zip(*map(list, strs)):
            if list(t) != sorted(t):
                ans += 1
        return ans 

'''
Runtime: 185 ms, faster than 70.95% of Python3 online submissions for Delete Columns to Make Sorted.
Memory Usage: 15.2 MB, less than 10.11% of Python3 online submissions for Delete Columns to Make Sorted.
'''
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        return sum(list(t) != sorted(t) for t in zip(*map(list, strs)))


'''
Runtime: 125 ms, faster than 91.79% of Python3 online submissions for Delete Columns to Make Sorted.
Memory Usage: 15.2 MB, less than 10.11% of Python3 online submissions for Delete Columns to Make Sorted.
'''
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ans = 0
        for t in zip(*map(list, strs)):
            for a, b in pairwise(t):
                if a > b:
                    ans += 1
                    break
        return ans 

'''
Runtime: 352 ms, faster than 47.58% of Python3 online submissions for Delete Columns to Make Sorted.
Memory Usage: 14.8 MB, less than 25.26% of Python3 online submissions for Delete Columns to Make Sorted.
'''
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ans = 0
        m, n = len(strs), len(strs[0])
        for j in range(n):
            for i in range(1, m):
                if strs[i][j] < strs[i - 1][j]:
                    ans += 1
                    break
        return ans 

        