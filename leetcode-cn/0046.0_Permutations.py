'''
approach: Backtracking
Time: O()

执行结果：通过
显示详情
执行用时：24 ms, 在所有 Python 提交中击败了50.04%的用户
内存消耗：13.3 MB, 在所有 Python 提交中击败了32.64%的用户
'''


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        permutations = []
        size = len(nums)
        def backtracking(nums, path, size):
            if len(path) == size:
                permutations.append(path)
                return
            for num in nums:
                if num not in path:
                    backtracking(nums, path + [num], size)

        backtracking(nums, [], size)
        return permutations


'''
bracktracking

执行用时：44 ms, 在所有 Python3 提交中击败了27.48% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了72.06% 的用户
通过测试用例：26 / 26
'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans, n = [], len(nums)

        def backtrack(cur):
            if len(cur) == n:
                ans.append(cur)
            for x in nums:
                if x not in cur:
                    backtrack(cur + [x])

        backtrack([])
        return ans 


'''
执行用时：36 ms, 在所有 Python3 提交中击败了78.56% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了45.71% 的用户
通过测试用例：26 / 26
'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans, n = [], len(nums)

        def backtrack(cur):
            if len(cur) == n:
                ans.append(cur)
            for x in nums:
                if x not in cur:
                    cur.append(x)
                    backtrack(cur[:])
                    cur.pop()

        backtrack([])
        return ans 


'''
mask

执行用时：40 ms, 在所有 Python3 提交中击败了55.08% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了70.50% 的用户
通过测试用例：26 / 26
'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans, n = [], len(nums)
        mask = (1 << n) - 1

        def backtrack(cur, state):
            if state == mask:
                ans.append(cur)
                return 
            for i, x in enumerate(nums):
                if (1 << i) & state == 0:
                    backtrack(cur + [x], state | (1 << i))

        backtrack([], 0)
        return ans 

'''
执行用时：28 ms, 在所有 Python3 提交中击败了98.22% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了97.49% 的用户
通过测试用例：26 / 26
'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(itertools.permutations(nums))
        