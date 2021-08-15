'''
sort

220 / 220 个通过测试用例
状态：通过
执行用时: 228 ms
内存消耗: 27.3 MB
提交时间：5 小时前
'''
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        l, r = 0, len(nums) - 1
        ans = []
        while l <= r:
            ans.append(nums[l])
            l += 1
            if l < r:
                ans.append(nums[r])
                r -= 1
        
        return ans

