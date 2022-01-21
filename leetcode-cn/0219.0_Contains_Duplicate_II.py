'''
hash table

执行用时：76 ms, 在所有 Python3 提交中击败了66.17% 的用户
内存消耗：25.9 MB, 在所有 Python3 提交中击败了45.63% 的用户
通过测试用例：51 / 51
'''
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        val2idx = dict()
        for i, x in enumerate(nums):
            if x in val2idx and i - val2idx[x] <= k:
                return True
            val2idx[x] = i 

        return False
