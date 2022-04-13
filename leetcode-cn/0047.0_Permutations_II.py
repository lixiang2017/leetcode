'''
backtrack + mask

执行用时：492 ms, 在所有 Python3 提交中击败了14.59% 的用户
内存消耗：15.6 MB, 在所有 Python3 提交中击败了5.12% 的用户
通过测试用例：33 / 33
'''
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = set()
        mask = (1 << n) - 1

        # cur_path, state denotes added indices
        def backtrack(cur, state):
            if state == mask:
                ans.add(tuple(cur))
            for j in range(n):
                if (state >> j) & 1 == 0:
                    backtrack(cur + [nums[j]], state | (1 << j))

        backtrack([], 0)
        return [list(p) for p in ans]


'''
sort + 记忆状态（相邻相同元素，确保前者已经添加过）

执行用时：52 ms, 在所有 Python3 提交中击败了43.60% 的用户
内存消耗：15.3 MB, 在所有 Python3 提交中击败了56.69% 的用户
通过测试用例：33 / 33
'''
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        nums.sort()
        visited = [0] * n

        # idx, cur_path
        def backtrack(idx, cur):
            if idx == n:
                ans.append(cur[:])
                return 
            for i in range(n):
                if visited[i] or (i > 0 and nums[i - 1] == nums[i] and not visited[i - 1]):
                    continue
                visited[i] = 1
                cur.append(nums[i])
                backtrack(idx + 1, cur)
                cur.pop()
                visited[i] = 0

        backtrack(0, [])
        return ans 


'''
sort + 记忆状态（相邻相同元素，确保前者已经添加过） + mask

执行用时：44 ms, 在所有 Python3 提交中击败了76.79% 的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了70.50% 的用户
通过测试用例：33 / 33
'''
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        nums.sort()

        # idx, cur_path
        def backtrack(idx, cur, visited):
            if idx == n:
                ans.append(cur)
                return 
            for i in range(n):
                if (visited >> i & 1) or (i > 0 and nums[i - 1] == nums[i] and not (visited >> (i-1) & 1)):
                    continue
                backtrack(idx + 1, cur + [nums[i]], visited | (1 << i))

        backtrack(0, [], 0)
        return ans 

'''
and (visited >> (i-1) & 1)

执行用时：88 ms, 在所有 Python3 提交中击败了21.56% 的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了73.21% 的用户
通过测试用例：33 / 33
'''
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        nums.sort()

        # idx, cur_path
        def backtrack(idx, cur, visited):
            if idx == n:
                ans.append(cur)
                return 
            for i in range(n):
                if (visited >> i & 1) or (i > 0 and nums[i - 1] == nums[i] and (visited >> (i-1) & 1)):
                    continue
                backtrack(idx + 1, cur + [nums[i]], visited | (1 << i))

        backtrack(0, [], 0)
        return ans 

'''
remove idx

执行用时：80 ms, 在所有 Python3 提交中击败了23.06% 的用户
内存消耗：15.3 MB, 在所有 Python3 提交中击败了58.47% 的用户
通过测试用例：33 / 33
'''
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        nums.sort()
        mask = (1 << n) - 1

        def backtrack(cur, visited):
            if visited == mask:
                ans.append(cur)
                return 
            for i in range(n):
                if (visited >> i & 1) or (i > 0 and nums[i - 1] == nums[i] and (visited >> (i-1) & 1)):
                    continue
                backtrack(cur + [nums[i]], visited | (1 << i))

        backtrack([], 0)
        return ans 


'''
remove idx, and not (visited >> (i-1) & 1)

执行用时：32 ms, 在所有 Python3 提交中击败了99.43% 的用户
内存消耗：15.3 MB, 在所有 Python3 提交中击败了50.34% 的用户
通过测试用例：33 / 33
'''
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        nums.sort()
        mask = (1 << n) - 1

        def backtrack(cur, visited):
            if visited == mask:
                ans.append(cur)
                return 
            for i in range(n):
                if (visited >> i & 1) or (i > 0 and nums[i - 1] == nums[i] and not (visited >> (i-1) & 1)):
                    continue
                backtrack(cur + [nums[i]], visited | (1 << i))

        backtrack([], 0)
        return ans 





