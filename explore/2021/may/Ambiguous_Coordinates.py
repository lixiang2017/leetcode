'''
Time: O(N^3)
Space: O(1)

You are here!
Your runtime beats 80.34 % of python3 submissions.
You are here!
Your memory usage beats 73.50 % of python3 submissions.
'''


class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        s = s[1: -1]
        def permuts(s):
            if not s or len(s) > 1 and s[0] == s[-1] == '0':
                return []
            if '0' == s[-1]:
                return [s]
            if '0' == s[0]:
                return ['0' + '.' + s[1:]]
            return [s] + [s[:i] + '.' + s[i:] for i in range(1, len(s))]
        
        return ['(%s, %s)' % (a, b) for i in range(len(s)) for a, b in itertools.product(permuts(s[:i]), permuts(s[i:]))]
