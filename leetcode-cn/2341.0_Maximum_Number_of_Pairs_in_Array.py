'''
hash table

执行用时：36 ms, 在所有 Python3 提交中击败了70.41% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了56.63% 的用户
通过测试用例：128 / 128
'''
class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        remove = left = 0
        c = Counter(nums)
        for _, cnt in c.items():
            remove += cnt // 2
            if cnt % 2:
                left += 1
        return [remove, left]

