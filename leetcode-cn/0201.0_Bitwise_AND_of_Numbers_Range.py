'''
approach: to find common prefix
Time: O(logN)
Space: O(1)

执行用时：60 ms, 在所有 Python3 提交中击败了81.69% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了42.12% 的用户
'''
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0
        while left < right:
            left >>= 1
            right >>= 1
            shift += 1
        return left << shift


'''
Brian Kernighan
Time: O(logN)
Space: O(1)
执行用时：64 ms, 在所有 Python3 提交中击败了70.87% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了17.71% 的用户
'''
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        while left < right:
            right &= (right - 1)
        return right
