'''
sort

执行用时：48 ms, 在所有 Python3 提交中击败了65.82% 的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了45.41% 的用户
通过测试用例：57 / 57
'''
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n, m = len(nums), len(queries)
        ans = [0] * m
        nums.sort()
        i = s = 0
        pairs = [(q, j) for j, q in enumerate(queries)]
        pairs.sort()
        for q, j in pairs:
            while i < n and s + nums[i] <= q:
                s += nums[i]
                i += 1
            ans[j] = i
        return ans 

'''
prefix sum + binary search

执行用时：36 ms, 在所有 Python3 提交中击败了97.45% 的用户
内存消耗：15.3 MB, 在所有 Python3 提交中击败了27.04% 的用户
通过测试用例：57 / 57
'''
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        pre = list(accumulate(sorted(nums)))
        return [bisect_right(pre, q) for q in queries]


'''
执行用时：44 ms, 在所有 Python3 提交中击败了80.61% 的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了60.71% 的用户
通过测试用例：57 / 57
'''
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        pre = list(accumulate(sorted(nums)))
        func = partial(bisect_right, pre)
        return list(map(func, queries))


