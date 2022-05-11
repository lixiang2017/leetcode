'''
backtracking

Runtime: 46 ms, faster than 46.09% of Python3 online submissions for Combination Sum III.
Memory Usage: 14 MB, less than 29.87% of Python3 online submissions for Combination Sum III.
'''
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        ans = []
        
        def dfs(arr, left):
            if left == 0 and len(arr) == k:
                ans.append(arr)
                return 
            if len(arr) > k:
                return 
            start = arr[-1] + 1 if len(arr) > 0 else 1
            for i in range(start, 10):
                if left >= i:
                    dfs(arr + [i], left - i)
        
        dfs([], n)
        return ans  



'''
backtrack

Runtime: 43 ms, faster than 54.48% of Python3 online submissions for Combination Sum III.
Memory Usage: 13.9 MB, less than 29.87% of Python3 online submissions for Combination Sum III.
'''
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        
        def backtrack(arr, left):
            if left == 0 and len(arr) == k:
                ans.append(arr[:])
                return 
            if len(arr) > k:
                return 
            start = arr[-1] + 1 if len(arr) > 0 else 1
            for i in range(start, 10):
                if left >= i:
                    arr.append(i)
                    backtrack(arr, left - i)
                    arr.pop()
        
        backtrack([], n)
        return ans  



'''
二进制枚举

Runtime: 59 ms, faster than 17.68% of Python3 online submissions for Combination Sum III.
Memory Usage: 13.9 MB, less than 29.87% of Python3 online submissions for Combination Sum III.
'''
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        
        def check(mask):
            comb = []
            for i in range(9):
                if (mask >> i) & 1:
                    comb.append(i + 1)
            if len(comb) == k and sum(comb) == n:
                return comb 
            else:
                return None 
            
        for m in range(1 << 9):
            one = check(m)
            if one:
                ans.append(one)
        return ans  
