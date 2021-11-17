'''
Bit Manipulation
T: O(N + N^2)
S: O(N)

执行用时：376 ms, 在所有 Python3 提交中击败了57.51% 的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了85.18% 的用户
通过测试用例：167 / 167
'''
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        N = len(words)
        ans, mask = 0, [0] * N
        for i, w in enumerate(words):
            for ch in w:
                mask[i] |= 1 << (ord(ch) - ord('a'))
        
        for i in range(1, N):
            for j in range(i):
                if mask[i] & mask[j] == 0:
                    ans = max(ans, len(words[i]) * len(words[j]))

        return ans

'''
sort + bit manipulation

执行用时：440 ms, 在所有 Python3 提交中击败了54.55% 的用户
内存消耗：15.4 MB, 在所有 Python3 提交中击败了34.39% 的用户
通过测试用例：167 / 167
'''
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        N = len(words)
        ans, mask = 0, [0] * N
        # sort by word len, descreasing
        words.sort(key=lambda w: -len(w))
        for i, w in enumerate(words):
            for ch in w:
                mask[i] |= 1 << (ord(ch) - ord('a'))
        
        for i in range(1, N):
            for j in range(i):
                if len(words[i]) * len(words[j]) <= ans:
                    break
                if mask[i] & mask[j] == 0:
                    ans = max(ans, len(words[i]) * len(words[j]))

        return ans


'''
sort + bit manipulation

执行用时：480 ms, 在所有 Python3 提交中击败了53.76% 的用户
内存消耗：15.3 MB, 在所有 Python3 提交中击败了72.93% 的用户
通过测试用例：167 / 167
'''
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        N = len(words)
        ans, mask = 0, [0] * N
        # sort by word len, descreasing
        words.sort(key=lambda w: -len(w))
        for i, w in enumerate(words):
            for ch in w:
                mask[i] |= 1 << (ord(ch) - ord('a'))
        
        for i in range(1, N):
            if len(words[i]) * len(words[0]) <= ans:
                break            
            for j in range(i):
                if len(words[i]) * len(words[j]) <= ans:
                    break
                if mask[i] & mask[j] == 0:
                    ans = max(ans, len(words[i]) * len(words[j]))

        return ans
