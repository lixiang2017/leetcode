'''
backtrack

执行用时：188 ms, 在所有 Python3 提交中击败了12.13% 的用户
内存消耗：22.2 MB, 在所有 Python3 提交中击败了40.35% 的用户
通过测试用例：30 / 30
'''
class Solution:
    def permutation(self, S: str) -> List[str]:
        n = len(S)
        mask = (1 << n) - 1
        ans = []

        def backtrack(cur, visited):
            if visited == mask:
                ans.append(cur)
                return
            for i in range(n):
                if visited >> i & 1 == 0:
                    backtrack(cur + S[i], visited | (1 << i))

        backtrack('', 0)
        return ans
    

'''
BFS

执行用时：272 ms, 在所有 Python3 提交中击败了5.94% 的用户
内存消耗：24.1 MB, 在所有 Python3 提交中击败了5.20% 的用户
通过测试用例：30 / 30
'''
class Solution:
    def permutation(self, S: str) -> List[str]:
        n = len(S)
        mask = (1 << n) - 1
        ans = []

        q = deque([('', 0)])
        while q:
            part, state = q.popleft()
            if state == mask:
                ans.append(part)
            for i in range(n):
                if state >> i & 1 == 0:
                    q.append((part + S[i], state | (1 << i)))
                
        return ans
    
'''
nextPermutation

执行用时：92 ms, 在所有 Python3 提交中击败了83.66% 的用户
内存消耗：21.6 MB, 在所有 Python3 提交中击败了85.64% 的用户
通过测试用例：30 / 30
'''
class Solution:
    def permutation(self, S: str) -> List[str]:
        n = len(S)
        s = sorted(list(S))
        ans = [''.join(s)]

        def nextPermutation():
            i = n - 2
            while i >= 0 and s[i] >= s[i + 1]:
                i -= 1
            if i == -1:
                return False
            # swap
            j = n - 1
            while s[i] >= s[j]:
                j -= 1
            s[i], s[j] = s[j], s[i]
            left, right = i + 1, n - 1
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            return True 

        while nextPermutation():
            ans.append(''.join(s))
        
        return ans

'''
pass by reference

执行用时：92 ms, 在所有 Python3 提交中击败了83.66% 的用户
内存消耗：21.6 MB, 在所有 Python3 提交中击败了86.14% 的用户
通过测试用例：30 / 30
'''
class Solution:
    def permutation(self, S: str) -> List[str]:
        n = len(S)
        ss = sorted(list(S))
        ans = [''.join(ss)]

        def nextPermutation(s: List[str]):
            # pass by reference
            i = n - 2
            while i >= 0 and s[i] >= s[i + 1]:
                i -= 1
            if i == -1:
                return False
            # swap
            j = n - 1
            while s[i] >= s[j]:
                j -= 1
            s[i], s[j] = s[j], s[i]
            left, right = i + 1, n - 1
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            return True 

        while nextPermutation(ss):
            ans.append(''.join(ss))
        
        return ans


