'''
置换环
simulation / brute force

置换环 同类型题目
https://leetcode.cn/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/

执行用时：392 ms, 在所有 Python3 提交中击败了42.86% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了71.43% 的用户
通过测试用例：66 / 66
'''
class Solution:
    def reinitializePermutation(self, n: int) -> int:
        init, perm = list(range(n)), list(range(n))
        arr = [0] * n
        op = 0
        while True:
            for i in range(n):
                if i % 2 == 0:
                    arr[i] = perm[i // 2]
                else:
                    arr[i] = perm[n // 2 + (i - 1) // 2]
            op += 1
            if arr == init:
                break
            else:
                perm = arr[:]
        return op 
