'''
backtrack
not (visited >> (i - 1) & 1) : 数值相同的数字，保证从左至右依次添加
## 下面这个应该会慢一些
(visited >> (i - 1) & 1) : 数值相同的数字，保证从右至左依次添加

Runtime: 80 ms, faster than 62.84% of Python3 online submissions for Permutations II.
Memory Usage: 14.5 MB, less than 23.43% of Python3 online submissions for Permutations II.
'''
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        permutes = []
        nums.sort()
        n = len(nums)
        all_visited = (1 << n) - 1
        visited = 0
        
        def backtrack(visited, curr):
            if visited == all_visited:
                permutes.append(curr)
                return 
            for i in range(n):
                if (visited >> i) & 1 or (i > 0 and nums[i - 1] == nums[i] and not (visited >> (i - 1) & 1)):
                    continue
                backtrack(visited | (1 << i), curr + [nums[i]])
        
        backtrack(0, [])
        return permutes


'''
Runtime: 143 ms, faster than 27.03% of Python3 online submissions for Permutations II.
Memory Usage: 14.6 MB, less than 10.49% of Python3 online submissions for Permutations II.
'''
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        permutes = []
        nums.sort()
        n = len(nums)
        all_visited = (1 << n) - 1
        visited = 0
        
        def backtrack(visited, curr):
            if visited == all_visited:
                permutes.append(curr)
                return 
            for i in range(n):
                if (visited >> i) & 1 or (i > 0 and nums[i - 1] == nums[i] and (visited >> (i - 1) & 1)):
                    continue
                backtrack(visited | (1 << i), curr + [nums[i]])
        
        backtrack(0, [])
        return permutes

'''
## i + 1 < n
not (visited >> (i + 1) & 1): 数值相同的数字，保证从右至左依次添加
(visited >> (i + 1) & 1): 数值相同的数字，保证从左至右依次添加

Runtime: 78 ms, faster than 64.93% of Python3 online submissions for Permutations II.
Memory Usage: 14.4 MB, less than 47.48% of Python3 online submissions for Permutations II.
'''
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        permutes = []
        nums.sort()
        n = len(nums)
        all_visited = (1 << n) - 1
        visited = 0
        
        def backtrack(visited, curr):
            if visited == all_visited:
                permutes.append(curr)
                return 
            for i in range(n):
                if (visited >> i) & 1 or (i + 1 < n and nums[i + 1] == nums[i] and not (visited >> (i + 1) & 1)):
                    continue
                backtrack(visited | (1 << i), curr + [nums[i]])
        
        backtrack(0, [])
        return permutes


'''
(visited >> (i + 1) & 1)

Runtime: 152 ms, faster than 26.19% of Python3 online submissions for Permutations II.
Memory Usage: 14.5 MB, less than 10.49% of Python3 online submissions for Permutations II.
'''
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        permutes = []
        nums.sort()
        n = len(nums)
        all_visited = (1 << n) - 1
        visited = 0
        
        def backtrack(visited, curr):
            if visited == all_visited:
                permutes.append(curr)
                return 
            for i in range(n):
                if (visited >> i) & 1 or (i + 1 < n and nums[i + 1] == nums[i] and (visited >> (i + 1) & 1)):
                    continue
                backtrack(visited | (1 << i), curr + [nums[i]])
        
        backtrack(0, [])
        return permutes


'''
for i in range(n - 1, -1, -1):
not (visited >> (i + 1) & 1)

Runtime: 76 ms, faster than 67.01% of Python3 online submissions for Permutations II.
Memory Usage: 14.4 MB, less than 23.43% of Python3 online submissions for Permutations II.
'''
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        permutes = []
        nums.sort()
        n = len(nums)
        all_visited = (1 << n) - 1
        visited = 0
        
        def backtrack(visited, curr):
            if visited == all_visited:
                permutes.append(curr)
                return 
            for i in range(n - 1, -1, -1):
                if (visited >> i) & 1 or (i + 1 < n and nums[i + 1] == nums[i] and not (visited >> (i + 1) & 1)):
                    continue
                backtrack(visited | (1 << i), curr + [nums[i]])
        
        backtrack(0, [])
        return permutes





