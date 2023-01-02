'''
hash table

执行用时：636 ms, 在所有 Python3 提交中击败了45.31% 的用户
内存消耗：43.4 MB, 在所有 Python3 提交中击败了20.31% 的用户
通过测试用例：37 / 37
'''
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        h = Counter()
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                h[nums[i] * nums[j]] += 1
        ans = 0
        for t, c in h.items():
            ans += c * (c - 1) // 2
        return ans * 8
