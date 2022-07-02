'''
Two Pointers

执行用时：32 ms, 在所有 Python3 提交中击败了89.55% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了57.98% 的用户
'''
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0
        M, N = len(s), len(t)
        while i < M and j < N:
            if s[i] != t[j]:
                j += 1
            else:
                i += 1
                j += 1
        return i == M


'''
执行用时：40 ms, 在所有 Python3 提交中击败了46.55% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了90.49% 的用户
通过测试用例：17 / 17
'''
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        it = iter(t)
        return all(ch in it for ch in s)


'''
执行用时：32 ms, 在所有 Python3 提交中击败了85.30% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了92.43% 的用户
通过测试用例：17 / 17
'''
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        loc = -1
        for ch in s:
            loc = t.find(ch, loc + 1)
            if loc == -1:
                return False
        return True
        

'''
执行用时：28 ms, 在所有 Python3 提交中击败了95.94% 的用户
内存消耗：15.4 MB, 在所有 Python3 提交中击败了26.07% 的用户
通过测试用例：17 / 17
'''
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        lookup = defaultdict(list)
        for idx, ch in enumerate(t):
            lookup[ch].append(idx)

        loc = -1
        for ch in s:
            j = bisect_left(lookup[ch], loc + 1)
            if j >= len(lookup[ch]):
                return False
            loc = lookup[ch][j]

        return True



'''
执行用时：36 ms, 在所有 Python3 提交中击败了85.63% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了90.77% 的用户
通过测试用例：17 / 17
'''
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False 
        it = iter(t)
        return all(need in it for need in s)


'''
two pointers
T: O(M + N)
S: O(1)

执行用时：40 ms, 在所有 Python3 提交中击败了67.79% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了56.38% 的用户
通过测试用例：17 / 17
'''
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False 
        m, n, i, j = len(s), len(t) , 0, 0
        while i < m and j < n:
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == m
            

'''
two pointers, iterate through t
T: O(M + N)
S: O(1)

执行用时：40 ms, 在所有 Python3 提交中击败了67.79% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了63.36% 的用户
通过测试用例：17 / 17
'''
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True 
        if len(s) > len(t):
            return False 
        m, i = len(s), 0
        for ch in t:
            if ch == s[i]:
                i += 1
            if i == m:
                return True 
        return False 
            

'''
two pointers, iterate through s

执行用时：40 ms, 在所有 Python3 提交中击败了67.79% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了77.41% 的用户
通过测试用例：17 / 17
'''
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False 
        n, j = len(t), 0
        for ch in s:
            while j < n and ch != t[j]:
                j += 1
            if j == n:
                return False
            else:
                j += 1
        return True 










