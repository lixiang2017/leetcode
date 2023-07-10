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



'''
执行用时：1056 ms, 在所有 Python3 提交中击败了26.00% 的用户
内存消耗：17.6 MB, 在所有 Python3 提交中击败了38.78% 的用户
通过测试用例：318 / 318
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        N = len(nums)
        for i in range(N):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, N - 1
            target = -nums[i]
            while l < r:
                if l > i + 1 and nums[l] == nums[l - 1]:
                    l += 1
                    continue
                if r < N - 1 and nums[r] == nums[r + 1]:
                    r -= 1
                    continue
                t = nums[l] + nums[r]
                if t == target:
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                elif t > target:
                    r -= 1
                else:
                    l += 1
        return ans
        


'''
执行用时：1368 ms, 在所有 Python3 提交中击败了17.27% 的用户
内存消耗：17.8 MB, 在所有 Python3 提交中击败了73.92% 的用户
通过测试用例：318 / 318
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)
        for i in range(n):
            # remove duplicate
            if i >= 1 and nums[i] == nums[i - 1]:
                continue
            j, k = i + 1, n - 1
            while j < k:
                # remove duplicate
                while j > i + 1 and j < k and nums[j] == nums[j - 1]:
                    j += 1
                while k < n - 1 and j < k and nums[k] == nums[k + 1]:
                    k -= 1
                if j >= k:
                    break
                s = nums[i] + nums[j] + nums[k]
                if s == 0:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                elif s > 0:
                    k -= 1
                else:
                    j += 1

        return ans 

'''
sort + two pointers

执行用时：2240 ms, 在所有 Python3 提交中击败了16.55% 的用户
内存消耗：19.1 MB, 在所有 Python3 提交中击败了55.11% 的用户
通过测试用例：312 / 312
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        for i, x in enumerate(nums):
            if i > 0 and x == nums[i - 1]:
                continue
            j, k = i + 1, n - 1
            while j < k:
                while j > i + 1 and j < k and nums[j] == nums[j - 1]:
                    j += 1
                while k < n - 1 and j < k and nums[k] == nums[k + 1]:
                    k -= 1
                if j >= k:
                    break
                _sum = x + nums[j] + nums[k]
                if _sum == 0:
                    ans.append([x, nums[j], nums[k]])
                    j += 1
                    k -= 1
                elif _sum < 0:
                    j += 1
                else:
                    k -= 1
        return ans 


