'''
approach: Reverse + Sort
Time: O(NlogN)
Space: O(1)

执行用时：44 ms, 在所有 Python 提交中击败了97.67%的用户
内存消耗：13.5 MB, 在所有 Python 提交中击败了53.49%的用户
'''


class Solution(object):
    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        words = sorted([word[::-1] for word in words])
        N = len(words)
        length = 0
        for i in range(N - 1):
            size = len(words[i])
            if words[i] == words[i + 1][:size]:
                continue
            length += size + 1

        return length + len(words[-1]) + 1
        