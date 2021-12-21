'''
执行用时：76 ms, 在所有 Python3 提交中击败了93.34% 的用户
内存消耗：17.8 MB, 在所有 Python3 提交中击败了22.43% 的用户
通过测试用例：92 / 92
'''
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        aset = set(list(range(1, n + 1)))
        indegree = [0] * (n + 1)
        for a, b in trust:
            aset.discard(a)
            indegree[b] += 1
        ds = list(filter(lambda p: indegree[p] == n - 1, aset))
        if len(ds) == 1:
            return ds[0]
        else:
            return -1


'''
next

In [3]: ??next
Docstring:
next(iterator[, default])

Return the next item from the iterator. If default is given and the iterator
is exhausted, it is returned instead of raising StopIteration.
Type:      builtin_function_or_method


执行用时：92 ms, 在所有 Python3 提交中击败了46.85% 的用户
内存消耗：17.4 MB, 在所有 Python3 提交中击败了90.77% 的用户
通过测试用例：92 / 92
'''
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indegree = Counter(b for _, b in trust)
        outdegree = Counter(a for a, _ in trust)
        return next((i for i in range(1, n + 1) if indegree[i] == n - 1 and outdegree[i] == 0), -1)
