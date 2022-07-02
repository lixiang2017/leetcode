'''
转化为 53. 最大子数组和

执行用时：268 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：29.8 MB, 在所有 Python3 提交中击败了100.00% 的用户
通过测试用例：34 / 34
'''
class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        return max(self.max_subarray(nums1, nums2), self.max_subarray(nums2, nums1))
    
    def max_subarray(self, nums1, nums2) -> int:
        ans = dp = total = 0
        for x, y in zip(nums1, nums2):
            total += x
            dp = max(0, dp + y - x)
            ans = max(ans, dp)
        return total + ans 
