'''
Sort + Two Pointers

执行用时：64 ms, 在所有 Python3 提交中击败了31.98% 的用户
内存消耗：18.7 MB, 在所有 Python3 提交中击败了5.08% 的用户
通过测试用例：34 / 34
'''
class Solution:
    def findSwapValues(self, array1: List[int], array2: List[int]) -> List[int]:
        array1.sort(), array2.sort()
        s1, s2 = sum(array1), sum(array2)
        diff = s1 - s2
        if diff % 2:
            return []
        diff //= 2
        i, j, L1, L2 = 0, 0, len(array1), len(array2)
        while i < L1 and j < L2:
            diff1 = array1[i] - array2[j]
            if diff1 == diff:
                return [array1[i], array2[j]]
            elif diff1 > diff:
                j += 1
            else:
                i += 1     
        return []

