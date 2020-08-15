'''
https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/550/week-2-august-8th-august-14th/3421/
You are here!
Your runtime beats 73.95 % of python submissions.
34 / 34 test cases passed.
    Status: Accepted
Runtime: 20 ms
Memory Usage: 12.6 MB
    
Submitted: 0 minutes ago
'''



class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if 0 == rowIndex:
            return [1]

        subResult = self.getRow(rowIndex - 1)
        ans = [1,]
        for i in xrange(len(subResult)-1):
            ans.append(subResult[i] + subResult[i + 1])
        ans.append(1)

        return ans


if __name__ == '__main__':
    rowIndex = 0
    assert Solution().getRow(rowIndex) == [1]

    rowIndex = 1
    assert Solution().getRow(rowIndex) == [1, 1]

    rowIndex = 2
    assert Solution().getRow(rowIndex) == [1, 2, 1]

    rowIndex = 3
    assert Solution().getRow(rowIndex) == [1, 3, 3, 1]

    rowIndex = 33
    print Solution().getRow(rowIndex)
# [1, 33, 528, 5456, 40920, 237336, 1107568, 4272048, 13884156, 38567100, 92561040, 193536720, 354817320, 573166440, 818809200, 1037158320, 1166803110, 1166803110, 1037158320, 818809200, 573166440, 354817320, 193536720, 92561040, 38567100, 13884156, 4272048, 1107568, 237336, 40920, 5456, 528, 33, 1]