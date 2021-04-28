'''
approach: Two Pointers
Time: O(46342)
Space: O(46342)

执行用时：1080 ms, 在所有 Python3 提交中击败了5.15%的用户
内存消耗：16.5 MB, 在所有 Python3 提交中击败了6.14%的用户
'''

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        squares = [i * i for i in range(46342)]
        left, right = 0, 46341
        while left <= right:
            if squares[left] + squares[right] > c:
                right -= 1
            elif squares[left] + squares[right] < c:
                left += 1
            else:
                return True

        return False
