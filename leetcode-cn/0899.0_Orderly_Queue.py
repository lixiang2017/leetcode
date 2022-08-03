'''
1. k == 1 时，只能轮转；
2. k > 1 时，可以实现任意两个元素交换；遂可实现冒泡排序。

e.g.:  k == 2
   c d e f g h
-> c [e f g h] d
-> [e f g h] d c
-> d c [e f g h] 跟最初比较，只是交换了c d.

执行用时：44 ms, 在所有 Python3 提交中击败了21.43% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了79.46% 的用户
通过测试用例：110 / 110
'''
class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k > 1:
            return ''.join(sorted(s))
        ans = s
        for i in range(len(s)):
            ans = min(ans, s[i: ] + s[: i])
        return ans 
