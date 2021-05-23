'''
approach: math
Time: O(logN)
Space: O(1)

执行用时：84 ms, 在所有 Python3 提交中击败了35.05% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了76.76% 的用户
'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        x_bak = x
        reverse = 0
        while x:
            reverse *= 10
            reverse += (x % 10)
            x //= 10
            
        return x_bak == reverse



'''
执行用时：80 ms, 在所有 Python3 提交中击败了46.20% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了30.70% 的用户
'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[:: -1]