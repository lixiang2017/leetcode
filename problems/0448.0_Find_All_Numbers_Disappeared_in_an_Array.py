'''
T: O(2N)
S: O(1)

ref:
https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/discuss/92955/Python-4-lines-with-short-explanation

Runtime: 372 ms, faster than 55.30% of Python3 online submissions for Find All Numbers Disappeared in an Array.
Memory Usage: 22.2 MB, less than 60.62% of Python3 online submissions for Find All Numbers Disappeared in an Array.
'''
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for x in nums:
            nums[abs(x) - 1] = -abs(nums[abs(x) - 1])
        return [i + 1 for i, x in enumerate(nums) if x > 0]



'''
Hash Set
T: O(2N)
S: O(N)

Runtime: 328 ms, faster than 92.64% of Python3 online submissions for Find All Numbers Disappeared in an Array.
Memory Usage: 24.3 MB, less than 31.46% of Python3 online submissions for Find All Numbers Disappeared in an Array.
'''
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        N, seen = len(nums), set(nums)
        return [i for i in range(1, N + 1) if i not in seen]



'''
T: O(2N)
S: O(1)

For each number i in nums,
we mark the number that i points as negative.
Then we filter the list, get all the indexes
who points to a positive number.
Since those indexes are not visited.


index:  0, 1, 2, 3, 4, 5, 6, 7
nums = [4, 3, 2, 7, 8, 2, 3, 1]
 -->   -4 -3 -2  -7      -3 -1
 -->      -3 -2

Runtime: 364 ms, faster than 60.25% of Python3 online submissions for Find All Numbers Disappeared in an Array.
Memory Usage: 22.3 MB, less than 51.93% of Python3 online submissions for Find All Numbers Disappeared in an Array.
'''

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for x in nums:
            idx = abs(x) - 1
            nums[idx] = -abs(nums[idx])
        return [i + 1 for i, x in enumerate(nums) if x > 0]

'''
use start index in enumerate

Runtime: 392 ms, faster than 36.43% of Python3 online submissions for Find All Numbers Disappeared in an Array.
Memory Usage: 22 MB, less than 63.98% of Python3 online submissions for Find All Numbers Disappeared in an Array.
'''
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for x in nums:
            idx = abs(x) - 1
            nums[idx] = -abs(nums[idx])
        return [i for i, x in enumerate(nums, start=1) if x > 0]

'''
Hash Set

Runtime: 328 ms, faster than 92.64% of Python3 online submissions for Find All Numbers Disappeared in an Array.
Memory Usage: 25.9 MB, less than 7.00% of Python3 online submissions for Find All Numbers Disappeared in an Array.
'''
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return set(range(1, len(nums) + 1)).difference(set(nums))

'''
Runtime: 324 ms, faster than 95.74% of Python3 online submissions for Find All Numbers Disappeared in an Array.
Memory Usage: 25.9 MB, less than 7.00% of Python3 online submissions for Find All Numbers Disappeared in an Array.
'''
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return set(range(1, len(nums) + 1)) - set(nums)
        
     


