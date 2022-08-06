'''
brute force

执行用时：40 ms, 在所有 Python3 提交中击败了71.43% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了81.11% 的用户
通过测试用例：67 / 67
'''
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key=len)
        n = len(words)
        ans = []

        def isSubstring(idx, w):
            for j in range(idx + 1, n):
                if len(words[j]) == len(w):
                    continue
                if w in words[j]:
                    return True 
            return False

        for i, w in enumerate(words):
            if isSubstring(i, w):
                ans.append(w)
        return ans 

