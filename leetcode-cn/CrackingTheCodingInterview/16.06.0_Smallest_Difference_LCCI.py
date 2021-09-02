'''
Sort + Binary Search + Two Pointers

执行用时：208 ms, 在所有 Python3 提交中击败了35.84% 的用户
内存消耗：21.2 MB, 在所有 Python3 提交中击败了27.60% 的用户
通过测试用例：60 / 60
'''
class Solution:
    def smallestDifference(self, a: List[int], b: List[int]) -> int:
        diff = float('inf')
        a.sort(), b.sort()
        N, M = len(a), len(b)
        i = j = 0
        l = r = 0
        while i < N:
            l, r = bisect_left(b, a[i], l), bisect_right(b, a[i], r)
            if l < M:
                diff = min(diff, abs(b[l] - a[i]))
            if r <= M:
                diff = min(diff, abs(b[r - 1] - a[i]))
            i += 1
        return diff

'''
输入：
[-2147483648,1]
[2147483647,0]
输出：
2147483646
预期结果：
1
'''

