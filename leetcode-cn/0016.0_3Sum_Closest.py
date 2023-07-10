'''
sort + two pointers
T: O(N^2)
S: O(1)

执行用时：200 ms, 在所有 Python3 提交中击败了20.68% 的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了9.70% 的用户
通过测试用例：131 / 131
'''
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        t = nums[0] + nums[1] + nums[-1]
        diff = abs(t - target)
        for i, x in enumerate(nums):
            j, k = i + 1, len(nums) - 1
            while j < k:
                t1 = x + nums[j] + nums[k]
                if abs(t1 - target) < diff:
                    t = t1 
                    diff = abs(t1 - target)
                if t1 <= target:
                    j += 1
                else:
                    k -= 1
        return t 

'''
直接return target
sort + two pointers
T: O(N^2)
S: O(1)

执行用时：80 ms, 在所有 Python3 提交中击败了78.14% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了94.98% 的用户
通过测试用例：131 / 131
'''
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        t = nums[0] + nums[1] + nums[-1]
        diff = abs(t - target)
        for i, x in enumerate(nums):
            j, k = i + 1, len(nums) - 1
            while j < k:
                t1 = x + nums[j] + nums[k]
                if abs(t1 - target) < diff:
                    t = t1 
                    diff = abs(t1 - target)
                if t1 < target:
                    j += 1
                elif t1 > target:
                    k -= 1
                else:
                    return target
        return t 


'''
if i j k same, continue

执行用时：84 ms, 在所有 Python3 提交中击败了70.54% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了50.22% 的用户
通过测试用例：131 / 131
'''
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        t = nums[0] + nums[1] + nums[-1]
        diff = abs(t - target)
        for i, x in enumerate(nums):
            if i > 0 and x == nums[i - 1]:
                continue
            j, k = i + 1, len(nums) - 1
            while j < k:
                while i + 1 < j < k and nums[j] == nums[j - 1]:
                    j += 1
                while j < k and k < len(nums) - 1 and nums[k] == nums[k + 1]:
                    k -= 1
                if j >= k:
                    break
                t1 = x + nums[j] + nums[k]
                if abs(t1 - target) < diff:
                    t = t1 
                    diff = abs(t1 - target)
                if t1 < target:
                    j += 1
                elif t1 > target:
                    k -= 1
                else:
                    return target
        return t 

'''
执行用时：668 ms, 在所有 Python3 提交中击败了74.87% 的用户
内存消耗：16 MB, 在所有 Python3 提交中击败了55.05% 的用户
通过测试用例：99 / 99
'''
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = sum(nums[: 3])
        n = len(nums)
        for i, x in enumerate(nums):
            j, k = i + 1, n - 1
            while j < k:
                s = x + nums[j] + nums[k]
                if s == target:
                    return s 
                elif s < target:
                    j += 1
                else:
                    k -= 1
                if abs(s - target) < abs(ans - target):
                    ans = s

        return ans 
