'''
approach: Set
Time: O(N)
Space: O(N) -> O(1)

执行用时：12 ms, 在所有 Python 提交中击败了90.16%的用户
内存消耗：12.8 MB, 在所有 Python 提交中击败了99.31%的用户
'''


class Solution(object):
    def isUnique(self, astr):
        """
        :type astr: str
        :rtype: bool
        """
        return len(set(astr)) == len(astr)

'''
approach: Hash Table
Time: O(N)
Space: O(N) -> O(1)

执行用时：20 ms, 在所有 Python 提交中击败了41.19%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了51.72%的用户
'''

class Solution(object):
    def isUnique(self, astr):
        """
        :type astr: str
        :rtype: bool
        """
        seen = defaultdict(bool)
        for letter in astr:
            if seen[letter]:
                return False
            seen[letter] = True
        return True


'''
approach: Bit Manipulation
Time: O(N)
Space: O(1)

执行用时：16 ms, 在所有 Python 提交中击败了71.40%的用户
内存消耗：13.2 MB, 在所有 Python 提交中击败了5.03%的用
'''


class Solution(object):
    def isUnique(self, astr):
        """
        :type astr: str
        :rtype: bool
        """
        checker = 0
        for letter in astr:
            val = ord(letter) - ord('a')
            if checker & (1 << val):
                return False
            checker |= (1 << val)
        return True

'''
approach: Brute Force
Time: O(N ^ 2)
Space: O(1)

执行用时：20 ms, 在所有 Python 提交中击败了41.19%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了55.61%的用户
'''

class Solution(object):
    def isUnique(self, astr):
        """
        :type astr: str
        :rtype: bool
        """
        N = len(astr)
        for i in range(N - 1):
            for j in range(i + 1, N):
                if astr[i] == astr[j]:
                    return False
        return True


'''
approach: Sort
Time: O(NlogN)
Space: O(1)

执行结果：
通过
显示详情
执行用时：12 ms, 在所有 Python 提交中击败了90.16%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了34.78%的用户
'''

class Solution(object):
    def isUnique(self, astr):
        """
        :type astr: str
        :rtype: bool
        """
        astr = sorted(list(astr))
        N = len(astr)
        for i in range(N - 1):
            if astr[i] == astr[i + 1]:
                return False
        return True
    