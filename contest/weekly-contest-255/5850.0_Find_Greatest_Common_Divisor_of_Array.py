'''
215 / 215 个通过测试用例
状态：通过
执行用时: 32 ms
内存消耗: 15.2 MB
提交时间：13 小时前
'''

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        maxn = max(nums)
        minn = min(nums)
        
        def gcd(a, b):
            if a % b == 0:
                return b
            else:
                return gcd(b, a % b)
        
        return gcd(maxn, minn)

