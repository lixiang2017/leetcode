'''
Time: O(N)
Space: O(N)

执行结果：
通过
显示详情
执行用时：
32 ms, 在所有 Python 提交中击败了40.63%的用户
内存消耗：
13 MB, 在所有 Python 提交中击败了65.63%的用户
'''

class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        firstHalf = s[: len(s) / 2]
        secondHalf = s[len(s) / 2: ]
        firstCount = secondCount = 0

        for char in firstHalf:
            if char in vowels:
                firstCount += 1
        
        for char in secondHalf:
            if char in vowels:
                secondCount += 1
        
        return firstCount == secondCount
