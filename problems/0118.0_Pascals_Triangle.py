'''
Success
Details
Runtime: 20 ms, faster than 46.94% of Python online submissions for Pascal's Triangle.
Memory Usage: 13.5 MB, less than 32.88% of Python online submissions for Pascal's Triangle.
'''



class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = [
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
        if numRows <= 5:
            return triangle[: numRows]
        
        for i in range(5, numRows):
            last_row = triangle[i - 1]
            last_row = [0] + last_row + [0]
            # length of last_row is i + 2
            new_row = []
            for j in range(1, i + 2):
                new_row.append(last_row[j - 1] + last_row[j])
                
            triangle.append(new_row)
        
        return triangle



'''
DP
T: O(N^2)
S: O(N^2)

Runtime: 61 ms, faster than 16.16% of Python3 online submissions for Pascal's Triangle.
Memory Usage: 13.9 MB, less than 17.88% of Python3 online submissions for Pascal's Triangle.
'''
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = [[1]]
        for _ in range(numRows - 1):
            pascal.append([a + b for a, b in pairwise([0] + pascal[-1] + [0])])
        return pascal 
