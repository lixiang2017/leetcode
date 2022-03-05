'''
DP
T: O(N)
S: O(1)

Runtime: 64 ms, faster than 29.90% of Python3 online submissions for Arithmetic Slices.
Memory Usage: 14.2 MB, less than 53.58% of Python3 online submissions for Arithmetic Slices.
'''
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        cnt, step = 1, None
        for i in range(1, n):
            if nums[i] - nums[i - 1] == step:
                '''
                2 -> 1
                3 -> 2
                '''
                cnt += 1
                ans += (cnt - 1)
            else:
                cnt = 1
                step = nums[i] - nums[i - 1]
                
        return ans

'''
[1,3,5,7,9]    6, not 7
135 357 579
1357  3579
13579
159     # no

[7,7,7,7]      3, not 4
'''


'''
Runtime: 30 ms, faster than 98.21% of Python3 online submissions for Arithmetic Slices.
Memory Usage: 14.1 MB, less than 97.59% of Python3 online submissions for Arithmetic Slices.
'''
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        cnt, step = 0, None
        for i in range(1, n):
            if nums[i] - nums[i - 1] == step:
                cnt += 1
                ans += cnt
            else:
                cnt = 0
                step = nums[i] - nums[i - 1]
                
        return ans


'''
Runtime: 72 ms, faster than 15.66% of Python3 online submissions for Arithmetic Slices.
Memory Usage: 14.1 MB, less than 75.02% of Python3 online submissions for Arithmetic Slices.
'''
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        d = defaultdict(int)
        n = len(nums)
        ans = 0
        for i in range(2, n):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                d[i] = d[i - 1] + 1
                ans += d[i]
        return ans 


'''
Runtime: 49 ms, faster than 63.49% of Python3 online submissions for Arithmetic Slices.
Memory Usage: 14.1 MB, less than 75.02% of Python3 online submissions for Arithmetic Slices.
'''
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        d = [0] * n
        ans = 0
        for i in range(2, n):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                d[i] = d[i - 1] + 1
                ans += d[i]
        return ans 

        