'''
stack
T: O(M + N)
S: O(M + N)

Success
Details 
Runtime: 24 ms, faster than 38.56% of Python online submissions for Backspace String Compare.
Memory Usage: 13.4 MB, less than 19.73% of Python online submissions for Backspace String Compare.
'''



class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        new_S = new_T = ""
        for ch in S:
            # if ch == '#' and new_S:   # Wrong Answer
                # new_S.pop()  # AttributeError: 'unicode' object has no attribute 'pop'
            if ch == '#':
                if new_S:
                    new_S = new_S[ : -1]
            else:
                new_S += ch
        for ch in T:
            # if ch == '#' and new_T:
                # new_T.pop()
            if ch == '#':
                if new_T:
                    new_T = new_T[ : -1]
            else:
                new_T += ch
        
        print 'new_S: ', new_S
        print 'new_T: ', new_T
        return new_S == new_T
    

    
'''
# new_S.pop()
AttributeError: 'unicode' object has no attribute 'pop'
    new_S.pop()
Line 11 in backspaceCompare (Solution.py)
    ret = Solution().backspaceCompare(param_1, param_2)
Line 44 in _driver (Solution.py)
    _driver()
Line 54 in <module> (Solution.py)
'''


'''
"y#fo##f"
"y#f#o##f"
'''


'''
stack

T: O(M + N)
S: O(M + N)

Runtime: 56 ms, faster than 18.05% of Python3 online submissions for Backspace String Compare.
Memory Usage: 13.9 MB, less than 77.17% of Python3 online submissions for Backspace String Compare.
'''
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def editor(s):
            ss = []
            for ch in s:
                if ch == '#':
                    if ss:
                        ss.pop()
                else:
                    ss.append(ch)
            return ''.join(ss)
    
        return editor(s) == editor(t)
        
'''
stack
T: O(M + N)
S: O(M + N)

Runtime: 30 ms, faster than 89.95% of Python3 online submissions for Backspace String Compare.
Memory Usage: 13.9 MB, less than 77.17% of Python3 online submissions for Backspace String Compare.
'''
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def editor(s):
            ss = []
            for ch in s:
                if ch == '#':
                    if ss:
                        ss.pop()
                else:
                    ss.append(ch)
            return ss
    
        return editor(s) == editor(t)
        

'''
two pointers
T: O(M + N)
S: O(1)

Runtime: 37 ms, faster than 66.62% of Python3 online submissions for Backspace String Compare.
Memory Usage: 13.9 MB, less than 77.18% of Python3 online submissions for Backspace String Compare.
'''
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # yield valid letters in a reversed way
        def f(u):
            skip = 0
            for ch in reversed(u):
                if ch == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield ch 
        
        return all(x == y for x, y in itertools.zip_longest(f(s), f(t)))









