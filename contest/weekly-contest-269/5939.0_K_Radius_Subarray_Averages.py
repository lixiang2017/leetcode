'''
36 / 36 个通过测试用例
状态：通过
执行用时: 336 ms
内存消耗: 31 MB
提交时间：13 小时前
'''
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        pre = list(accumulate(nums))
        n = len(nums)
        ans = []
        for i in range(n):
            l, r = i - k, i + k
            if l < 0 or r >= n:
                ans.append(-1)
            else:
                if l == 0:
                    s = pre[r]
                else:
                    s = pre[r] - pre[l - 1]
                ans.append(s // (2 * k + 1))
        
        return ans

