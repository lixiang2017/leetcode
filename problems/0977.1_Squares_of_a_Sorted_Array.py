'''
Two Pointers
T: O(2N)
S: O(N)

Runtime: 275 ms, faster than 38.03% of Python3 online submissions for Squares of a Sorted Array.
Memory Usage: 16.2 MB, less than 56.28% of Python3 online submissions for Squares of a Sorted Array.
'''
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        min_idx = 0
        for i, num in enumerate(nums):
            if abs(num) <= abs(nums[min_idx]):
                min_idx = i
            else:
                break
                
        ans = []
        i, j, n = min_idx, min_idx + 1, len(nums)
        while i >= 0 and j < n:
            i2, j2 = nums[i] ** 2, nums[j] ** 2
            if i2 < j2:
                ans.append(i2)
                i -= 1
            elif i2 > j2:
                ans.append(j2)
                j += 1
            else:
                ans.append(i2)
                ans.append(j2)
                i -= 1
                j += 1
        while i >= 0:
            ans.append(nums[i] ** 2)
            i -= 1
        while j < n:
            ans.append(nums[j] ** 2)
            j += 1
        return ans


'''
Two Pointers
T: O(N)
S: O(N)

Runtime: 402 ms, faster than 13.33% of Python3 online submissions for Squares of a Sorted Array.
Memory Usage: 16.1 MB, less than 74.10% of Python3 online submissions for Squares of a Sorted Array.
'''
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r, ans = 0, len(nums) - 1,  [0] * len(nums)
        while l <= r:
            la, ra = abs(nums[l]), abs(nums[r])
            ans[r - l] = max(la, ra) ** 2
            l, r = l + (la > ra), r - (la <= ra)
        return ans


'''
Two Pointers
T: O(N)
S: O(N)

Runtime: 281 ms, faster than 35.85% of Python3 online submissions for Squares of a Sorted Array.
Memory Usage: 16.2 MB, less than 31.01% of Python3 online submissions for Squares of a Sorted Array.
'''
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r, ans = 0, len(nums) - 1,  [0] * len(nums)
        while l <= r:
            la, ra = abs(nums[l]), abs(nums[r])
            ans[r - l] = max(la, ra) ** 2
            l, r = l + (la >= ra), r - (la < ra)
        return ans


'''
Runtime: 339 ms, faster than 22.87% of Python3 online submissions for Squares of a Sorted Array.
Memory Usage: 15.6 MB, less than 97.22% of Python3 online submissions for Squares of a Sorted Array.
'''
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums.sort(key=abs)
        for i in range(len(nums)):
            nums[i] **= 2
        return nums


'''
Runtime: 322 ms, faster than 50.87% of Python3 online submissions for Squares of a Sorted Array.
Memory Usage: 16.4 MB, less than 16.86% of Python3 online submissions for Squares of a Sorted Array.
'''
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        l, r = 0, n - 1
        while l <= r:
            left, right = abs(nums[l]), abs(nums[r])
            ans[r - l] = max(left, right) ** 2
            l += (left > right)
            r -= (left <= right)
        return ans 
    
    

