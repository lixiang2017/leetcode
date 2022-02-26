'''
iteration

Runtime: 52 ms, faster than 38.04% of Python3 online submissions for Subsets.
Memory Usage: 14.1 MB, less than 82.34% of Python3 online submissions for Subsets.
'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for x in nums:
            for i in range(len(ans)):
                ans.append(ans[i] + [x])
        return ans


'''
recursion

Runtime: 28 ms, faster than 97.49% of Python3 online submissions for Subsets.
Memory Usage: 14.2 MB, less than 69.11% of Python3 online submissions for Subsets.
'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        
        def dfs(i):
            if i == len(nums):
                return
            for j in range(len(ans)):
                ans.append(ans[j] + [nums[i]])
            dfs(i + 1)
            
        dfs(0)
        return ans


'''
Runtime: 42 ms, faster than 56.84% of Python3 online submissions for Subsets.
Memory Usage: 14.1 MB, less than 95.43% of Python3 online submissions for Subsets.
'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for x in nums:
            ans += [a + [x] for a in ans]
        return ans


'''
Runtime: 32 ms, faster than 91.39% of Python3 online submissions for Subsets.
Memory Usage: 14.1 MB, less than 82.34% of Python3 online submissions for Subsets.
'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        for i in range(2**n, 2**(n+1)):
            bitmask = bin(i)[3:]
            ans.append([nums[j] for j, b in enumerate(bitmask) if b == '1'])    
        return ans
        
        

