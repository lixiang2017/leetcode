'''
DP
T: O(N)
S: O(N^2)


Runtime: 50 ms, faster than 44.44% of Python3 online submissions for Pascal's Triangle II.
Memory Usage: 13.8 MB, less than 61.64% of Python3 online submissions for Pascal's Triangle II.
'''
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for _ in range(rowIndex):
            row = [a + b for a, b in pairwise([0] + row + [0])]
        return row 
