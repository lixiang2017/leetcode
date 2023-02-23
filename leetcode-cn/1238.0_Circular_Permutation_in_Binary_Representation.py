'''
执行用时：160 ms, 在所有 Python3 提交中击败了83.05% 的用户
内存消耗：23.1 MB, 在所有 Python3 提交中击败了72.88% 的用户
通过测试用例：47 / 47
'''
class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        arr = [0]
        for i in range(n):
            arr += [x + (1 << i) for x in reversed(arr)]
        idx = arr.index(start)
        return arr[idx: ] + arr[: idx]


'''
执行用时：152 ms, 在所有 Python3 提交中击败了93.22% 的用户
内存消耗：23.5 MB, 在所有 Python3 提交中击败了30.51% 的用户
通过测试用例：47 / 47
'''
class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        arr = [0]
        for i in range(n):
            arr += [x + (1 << i) for x in reversed(arr)]
        return [x ^ start for x in arr]

'''
从start开始。每个数字，先 ^start 恢复成原本模样，再加上最高位 |(1<<i)，再恢复回去 ^start.

执行用时：200 ms, 在所有 Python3 提交中击败了33.90% 的用户
内存消耗：23.2 MB, 在所有 Python3 提交中击败了47.46% 的用户
通过测试用例：47 / 47
'''
class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        arr = [start]
        for i in range(n):
            arr += [((x ^ start) | (1 << i)) ^ start for x in reversed(arr)]
        return arr


'''
Gray Code
理解格雷码的变化与自然数位数变化的不同，慢慢感受格雷码中位数变化的美妙。
格雷码转换之相邻异或消除多位改变
https://leetcode.cn/problems/circular-permutation-in-binary-representation/solution/javage-lei-ma-zhuan-huan-zhi-xiang-lin-y-j5ox/


执行用时：152 ms, 在所有 Python3 提交中击败了93.22% 的用户
内存消耗：23 MB, 在所有 Python3 提交中击败了83.05% 的用户
通过测试用例：47 / 47
'''
class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        return [i ^ (i >> 1) ^ start for i in range(1 << n)]
