'''
two pointers
T: O(N)
S: O(1)

48ms 击败 33.88%使用 Python3 的用户
15.78MB 击败 15.70%使用 Python3 的用户
'''
class Solution:
    def captureForts(self, forts: List[int]) -> int:
        ans = i = j = 0
        n = len(forts)
        while i < n:
            while i < n and forts[i] == 0:
                i += 1
            j = i + 1
            while j < n and forts[j] == 0:
                j += 1
            if j < n and forts[i] + forts[j] == 0:
                ans = max(ans, j - i - 1)
            i = j
        return ans 


'''
40ms 击败 81.82%使用 Python3 的用户
15.74MB 击败 26.45%使用 Python3 的用户
'''
class Solution:
    def captureForts(self, forts: List[int]) -> int:
        ans, pre = 0, -1
        for i, fort in enumerate(forts):
            if fort != 0:
                if pre >= 0 and fort != forts[pre]:
                    ans = max(ans, i - pre - 1)
                pre = i 
        return ans 
