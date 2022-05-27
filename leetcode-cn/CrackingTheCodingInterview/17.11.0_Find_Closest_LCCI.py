'''
two pointers
T: O(2N)
S: O(N)

执行用时：72 ms, 在所有 Python3 提交中击败了97.34% 的用户
内存消耗：31 MB, 在所有 Python3 提交中击败了30.04% 的用户
通过测试用例：43 / 43
'''
class Solution:
    def findClosest(self, words: List[str], word1: str, word2: str) -> int:
        n = len(words)
        p1, p2 = [], []
        for i, w in enumerate(words):
            if w == word1:
                p1.append(i)
            if w == word2:
                p2.append(i)
        if not p1 or not p2:
            return -1
        if word1 == word2:
            return 0 

        ans = n 
        n1, n2 = len(p1), len(p2)
        i = j = 0
        while i < n1 and j < n2:
            while j < n2 and p2[j] <= p1[i]:
                ans = min(ans, p1[i] - p2[j])
                j += 1
            if j < n2:
                ans = min(ans, p2[j] - p1[i])
            if j > 0:
                j -= 1
            i += 1
        return ans 


'''
two pointers
T: O(2N)
S: O(N)

执行用时：68 ms, 在所有 Python3 提交中击败了99.21% 的用户
内存消耗：31 MB, 在所有 Python3 提交中击败了24.41% 的用户
通过测试用例：43 / 43
'''
class Solution:
    def findClosest(self, words: List[str], word1: str, word2: str) -> int:
        n = len(words)
        p1, p2 = [], []
        for i, w in enumerate(words):
            if w == word1:
                p1.append(i)
            if w == word2:
                p2.append(i)
        if not p1 or not p2:
            return -1
        if word1 == word2:
            return 0 

        ans = n 
        n1, n2 = len(p1), len(p2)
        i = j = 0
        while i < n1 and j < n2:
            if i < n1 and j < n2 and p2[j] < p1[i]:
                ans = min(ans, p1[i] - p2[j])
                j += 1
            if i < n1 and j < n2 and p2[j] > p1[i]:
                ans = min(ans, p2[j] - p1[i])
                i += 1
        return ans 

'''
one pass
T: O(N)
S: O(1)
s
执行用时：88 ms, 在所有 Python3 提交中击败了73.62% 的用户
内存消耗：30.7 MB, 在所有 Python3 提交中击败了94.49% 的用户
通过测试用例：43 / 43
'''
class Solution:
    def findClosest(self, words: List[str], word1: str, word2: str) -> int:
        ans, n, p1, p2 = float('inf'), len(words), -float('inf'), float('inf')
        for i, w in enumerate(words):
            if w == word1:
                p1 = i 
                ans = min(ans, abs(p1 - p2))
            if w == word2:
                p2 = i 
                ans = min(ans, abs(p1 - p2))
        return ans



'''
remove abs

执行用时：72 ms, 在所有 Python3 提交中击败了97.24% 的用户
内存消耗：30.9 MB, 在所有 Python3 提交中击败了60.24% 的用户
通过测试用例：43 / 43
'''
class Solution:
    def findClosest(self, words: List[str], word1: str, word2: str) -> int:
        ans, n, p1, p2 = float('inf'), len(words), -float('inf'), -float('inf')
        for i, w in enumerate(words):
            if w == word1:
                p1 = i 
                ans = min(ans, p1 - p2)
            if w == word2:
                p2 = i 
                ans = min(ans, p2 - p1)
        return ans





