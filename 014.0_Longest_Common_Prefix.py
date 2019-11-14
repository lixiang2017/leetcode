'''
Author: lixiang
Beats: 86.54%
'''

import sys


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        minLength = sys.maxsize
        count = len(strs)

        if count == 0:
            return ""

        for str in strs:
            if minLength > len(str):
                minLength = len(str)

        i = 0
        flag = True
        while i < minLength:
            c = strs[0][i]
            for str in strs:
                if c != str[i]:
                    flag = False
                    break

            if flag == False:
                break
            else:
                i += 1

        return strs[0][:i]


if __name__ == "__main__":
    strs = ["flower", "flow", "flight"]
    print(Solution().longestCommonPrefix(strs))

    strs = ["dog", "racecar", "car"]
    print(Solution().longestCommonPrefix(strs))

    strs = []
    print(Solution().longestCommonPrefix(strs))
