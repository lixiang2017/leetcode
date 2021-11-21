'''
Brute Force, T:O(N^2),S:O(1)

126 / 126 个通过测试用例
状态：通过
执行用时: 56 ms
内存消耗: 14.9 MB
提交时间：12 小时前
'''
class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        ans = 0
        for i, c1 in enumerate(colors):
            for j, c2 in enumerate(colors):
                if c1 != c2:
                    ans = max(ans, abs(i - j))
        
        return ans



'''
Greedy,T:O(N),S:O(1)

执行用时：32 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了100.00% 的用户
通过测试用例：126 / 126
'''
class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        N = len(colors)
        if colors[0] != colors[-1]:
            return N - 1
        l, r = 0, N - 1
        while colors[l] == colors[N - 1]:
            l += 1
        while colors[0] == colors[r]:
            r -= 1
        return max(r, N - l - 1)

