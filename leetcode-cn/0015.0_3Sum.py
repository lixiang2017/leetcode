'''
Sort + Two Pointers
T: O(NlogN + N^2)

执行用时：1380 ms, 在所有 Python3 提交中击败了19.52% 的用户
内存消耗：17.5 MB, 在所有 Python3 提交中击败了55.77% 的用户
通过测试用例：318 / 318
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]: 
        ans = []
        nums.sort()
        N = len(nums)
        for i in range(N):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            t = 0 - nums[i]
            l, r = i + 1, N - 1
            while l < r:
                while l < r and l > i + 1 and nums[l] == nums[l - 1]:
                    l += 1
                while l < r and r < N - 1 and nums[r] == nums[r + 1]:
                    r -= 1
                if l >= r:  # need
                    break
                total = nums[l] + nums[r]
                if total == t:
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                elif total > t:
                    r -= 1
                else:
                    l += 1

        return ans

'''
通过测试用例：151 / 318
输入：
[-2,0,0,2,2]
输出：
[[-2,0,2],[0,0,0]]
预期结果：
[[-2,0,2]]
'''
