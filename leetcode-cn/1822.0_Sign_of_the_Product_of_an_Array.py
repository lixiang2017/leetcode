'''
执行用时：36 ms, 在所有 Python3 提交中击败了73.20% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了32.20% 的用户
通过测试用例：76 / 76
'''
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        neg_cnt = zero_cnt = 0
        for x in nums:
            if x == 0:
                zero_cnt = 1
                break
            elif x < 0:
                neg_cnt += 1
        
        return 0 if zero_cnt else -1 if neg_cnt % 2 else 1

'''
执行用时：40 ms, 在所有 Python3 提交中击败了47.54% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了70.36% 的用户
通过测试用例：76 / 76
'''
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        neg_cnt = 0
        for x in nums:
            if x == 0:
                return 0
            elif x < 0:
                neg_cnt += 1
        
        return -1 if neg_cnt % 2 else 1

