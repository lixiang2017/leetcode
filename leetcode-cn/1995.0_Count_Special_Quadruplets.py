'''
no need to sort
T: O(N^4)
S: O(1)

执行用时：1204 ms, 在所有 Python3 提交中击败了19.72% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了90.31% 的用户
通过测试用例：211 / 211
'''
class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        # nums.sort()
        n = len(nums)
        ans = 0
        # i j k l
        for i in range(n - 3):
            for j in range(i + 1, n - 2):
                for k in range(j + 1, n - 1):
                    for l in range(k + 1, n):
                        if nums[i] + nums[j] + nums[k] == nums[l]:
                            ans += 1
        return ans 
