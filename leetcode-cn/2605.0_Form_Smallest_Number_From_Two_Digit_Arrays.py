'''
56ms 击败 11.23%使用 Python3 的用户
15.53MB 击败 83.96%使用 Python3 的用户
'''
class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        if common := set(nums1) & set(nums2):
            return min(common)
        m1, m2 = min(nums1), min(nums2)
        if m1 > m2:
            m1, m2 = m2, m1
        return 10 * m1 + m2 
