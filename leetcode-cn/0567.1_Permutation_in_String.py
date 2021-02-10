'''
approach: Two Pointers / Sliding Window + Hash Table
Time: O(M + N)
Space: O(M + N + 26 + 26) = O(M + N)

执行结果：通过
显示详情
执行用时：76 ms, 在所有 Python 提交中击败了49.49%的用户
内存消耗：13.7 MB, 在所有 Python 提交中击败了5.61%的用户
'''


class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        pattern, text = list(s1), list(s2)
        pLen, tLen = len(s1), len(s2)
        pFreq = [0] * 26
        winFreq = [0] * 26
        for p in pattern:
            pFreq[ord(p) - ord('a')] += 1

        pCount = sum([1 for freq in pFreq if freq > 0])
        winCount = 0
        left = right = 0
        while right < tLen:
            if pFreq[ord(text[right]) - ord('a')] > 0:
                winFreq[ord(text[right]) - ord('a')] +=1 
                if winFreq[ord(text[right]) - ord('a')] == \
                        pFreq[ord(text[right]) - ord('a')]:
                    winCount += 1
            right += 1

            while pCount == winCount:
                if pLen == right - left:
                    return True
                if pFreq[ord(text[left]) - ord('a')] > 0:
                    winFreq[ord(text[left]) - ord('a')] -= 1
                    if winFreq[ord(text[left]) - ord('a')] \
                            < pFreq[ord(text[left]) - ord('a')]:
                        winCount -= 1
                left += 1
        
        return False
