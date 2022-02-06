'''
执行用时：60 ms, 在所有 Python3 提交中击败了8.99% 的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了69.10% 的用户
通过测试用例：43 / 43
'''
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s2t, t2s = {}, {}
        for ss, tt in zip(s, t):
            if (ss in s2t and tt not in t2s) or (ss not in s2t and tt in t2s):
                return False
            if ss in s2t and tt in t2s and (s2t[ss] != tt or t2s[tt] != ss):
                return False
            s2t[ss] = tt
            t2s[tt] = ss 
        return True

 '''
执行用时：40 ms, 在所有 Python3 提交中击败了72.92% 的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了77.54% 的用户
通过测试用例：43 / 43
 '''
 class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(s)) == len(set(t)) == len(set(zip(s, t)))       
        