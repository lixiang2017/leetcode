'''
执行用时：272 ms, 在所有 Python3 提交中击败了70.39% 的用户
内存消耗：17.4 MB, 在所有 Python3 提交中击败了51.40% 的用户
通过测试用例：12 / 12
'''

# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        x = self.rand49()
        # => [1, 40]
        while x > 40:
            x = self.rand49()
        return x % 10 + 1
    
    def rand49(self):
        # [1, 49]
        x = (rand7() - 1) * 7 + rand7()
        return x
