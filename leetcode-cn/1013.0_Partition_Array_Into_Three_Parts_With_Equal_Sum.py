'''
two pointers

执行用时：56 ms, 在所有 Python3 提交中击败了69.15% 的用户
内存消耗：20.8 MB, 在所有 Python3 提交中击败了32.66% 的用户
通过测试用例：72 / 72
'''
class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        three = sum(arr)
        if three % 3:
            return False
        one = three // 3
        i, _sum1, n = 1, arr[0], len(arr)
        while i < n and _sum1 != one:
            _sum1 += arr[i]
            i += 1

        j, _sum2 = n - 2, arr[n - 1]
        while j >= i and _sum2 != one:
            _sum2 += arr[j]
            j -= 1
        
        return one == _sum1 == _sum2 and i <= j

