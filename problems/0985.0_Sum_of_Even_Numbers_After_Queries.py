'''
simulation
T: O(N)
S: O(N)

Runtime: 1172 ms, faster than 19.64% of Python3 online submissions for Sum of Even Numbers After Queries.
Memory Usage: 20.5 MB, less than 75.51% of Python3 online submissions for Sum of Even Numbers After Queries.
'''
class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even = sum(x if x % 2 == 0 else 0 for x in nums)
        ans = []
        for val, i in queries:
            if nums[i] % 2 == 0 and val % 2 == 0:
                even += val 
            elif nums[i] % 2 == 0 and val % 2 == 1:
                even -= nums[i]
            elif nums[i] % 2 == 1 and val % 2 == 1:
                even += nums[i] + val
            nums[i] += val 
            ans.append(even)
        return ans 
