'''
approach: backtracking

执行用时：24 ms, 在所有 Python 提交中击败了72.35% 的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了71.36% 的用户
'''


class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.N = len(s)
        self.valids = []

        def backtracking(s, startIdx, currentPart, path):
            if len(path) == 4:
                return

            if len(path) == 3:
                currentLen = len(currentPart)
                decimal = int(''.join(currentPart))
                if len(''.join(path) + ''.join(currentPart)) == self.N and len(str(decimal)) == currentLen and decimal <= 255:
                    self.valids.append('.'.join(path) + '.' + ''.join(currentPart))
                    return

            # reach the end of s
            if startIdx > self.N - 1:
                return 

            currentLen = len(currentPart)
            if currentLen > 3:
                return
            if 0 < currentLen <= 3:
                decimal = int(''.join(currentPart))
                if len(str(decimal)) < currentLen or decimal > 255:  # invalid
                    return
                backtracking(s, startIdx + 1, currentPart + [s[startIdx]], path)
                backtracking(s, startIdx + 1, [s[startIdx]], path + [str(decimal)])
            elif 0 == currentLen:
                backtracking(s, startIdx + 1, [s[startIdx]], path)

        backtracking(s, 0, [], [])
      
        return self.valids