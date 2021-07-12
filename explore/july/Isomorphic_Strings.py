'''
Hash Table
Time: O(N)
Space: O(N)

You are here!
Your runtime beats 88.16 % of python3 submissions.
You are here!
Your memory usage beats 47.08 % of python3 submissions.
'''
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s2t, t2s = {}, {}
        for ss, tt in zip(s, t):
            if ss not in s2t and tt not in t2s:
                s2t[ss] = tt
                t2s[tt] = ss
            elif ss in s2t and tt in t2s:
                if s2t[ss] == tt and t2s[tt] == ss:
                    continue
                else:
                    return False
            else:
                return False
            
        return True
        