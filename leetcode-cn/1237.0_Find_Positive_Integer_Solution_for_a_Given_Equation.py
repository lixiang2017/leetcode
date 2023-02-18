'''
two pointers

执行用时：52 ms, 在所有 Python3 提交中击败了57.35% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了75.00% 的用户
通过测试用例：45 / 45
'''
"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        ans = []
        y = 1000
        for x in range(1, 1001):
            while y > 0 and (res := customfunction.f(x, y)) > z:
                y -= 1
            if y == 0:
                break
            if res == z:
                ans.append([x, y])
        return ans 

'''
range(1, z + 1)
y = z + 1

执行用时：44 ms, 在所有 Python3 提交中击败了80.88% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了45.59% 的用户
通过测试用例：45 / 45
'''
"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        ans = []
        y = z + 1
        for x in range(1, z + 1):
            while y > 0 and (res := customfunction.f(x, y)) > z:
                y -= 1
            if y == 0:
                break
            if res == z:
                ans.append([x, y])
        return ans 
        