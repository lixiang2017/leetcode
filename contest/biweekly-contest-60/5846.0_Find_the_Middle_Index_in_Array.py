'''
294 / 294 个通过测试用例
状态：通过
执行用时: 32 ms
内存消耗: 14.9 MB
提交时间：2 小时前
'''
class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        pre = [0] + list(accumulate(nums))
        pre += [pre[-1]]
        
        for i in range(1, len(nums) + 1):
            left = pre[i - 1]
            right = pre[-1] - pre[i]
            if left == right:
                return i - 1
        return -1
            
