#
# @lc app=leetcode id=984 lang=python
#
# [984] String Without AAA or BBB
#
'''
Success
Details 
Runtime: 12 ms, faster than 94.05% of Python online submissions for String Without AAA or BBB.
Memory Usage: 11.8 MB, less than 66.67% of Python online submissions for String Without AAA or BBB.
'''

# @lc code=start
class Solution(object):
    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        # print '=== A, B', A, B
        _len = A + B
        a, b = ('a', 'b') if A > B else ('b', 'a')
        # print a, b
        A, B = (A, B) if A > B else (B, A)
        ab = [a + b] * B
        # print ab
        A -= B
        res = []
        while A:
            res.append(a)
            if ab:
                res.append(ab.pop())
            A -= 1
        res += ab    
        # print 'res: ', ''.join(res) 
        return ''.join(res)

# @lc code=end

if __name__ == '__main__':
    A = 1
    B = 2
    print Solution().strWithout3a3b(A, B)
    # assert Solution().strWithout3a3b(A, B) == "abb"

    A = 4
    B = 1
    print Solution().strWithout3a3b(A, B)
    # assert Solution().strWithout3a3b(A, B) == "aabaa"

    A = 1
    B = 4
    print Solution().strWithout3a3b(A, B)


    A = 2
    B = 6
    print Solution().strWithout3a3b(A, B)

    A = 6
    B = 2
    print Solution().strWithout3a3b(A, B)

    A = 1
    B = 1
    print Solution().strWithout3a3b(A, B)
