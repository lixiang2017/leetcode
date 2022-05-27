'''
backtracking
从 0 开始

执行用时：340 ms, 在所有 Python3 提交中击败了42.35% 的用户
内存消耗：16.6 MB, 在所有 Python3 提交中击败了33.66% 的用户
通过测试用例：27 / 27
'''
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def backtrack(i, cur_arr) -> None:
            if k == len(cur_arr):
                ans.append(cur_arr)
                return 
            for j in range(i + 1, n + 1):
                backtrack(j, cur_arr + [j])

        backtrack(0, [])
        return ans 


'''
backtracking
从 1 开始

执行用时：336 ms, 在所有 Python3 提交中击败了45.63% 的用户
内存消耗：16.6 MB, 在所有 Python3 提交中击败了41.72% 的用户
通过测试用例：27 / 27
'''
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def backtrack(i, cur_arr) -> None:
            if k == len(cur_arr):
                ans.append(cur_arr)
                return 
            for j in range(i, n + 1):
                backtrack(j + 1, cur_arr + [j])

        backtrack(1, [])
        return ans 

'''
优化1，至少从n + 1 - (k - len(cur_arr)) + 1开始

执行用时：44 ms, 在所有 Python3 提交中击败了92.25% 的用户
内存消耗：16.5 MB, 在所有 Python3 提交中击败了67.18% 的用户
通过测试用例：27 / 27
'''
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def backtrack(i, cur_arr) -> None:
            if k == len(cur_arr):
                ans.append(cur_arr)
                return 
            for j in range(i, n + 1 - (k - len(cur_arr)) + 1):
                backtrack(j + 1, cur_arr + [j])

        backtrack(1, [])
        return ans


