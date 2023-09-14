'''
44 ms
15.8 MB
'''
class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, 1], [-1, -1], [1, -1], [1 ,1]]
        ans = []
        for i in range(8):
            x, y = king 
            while True:
                x += dirs[i][0]
                y += dirs[i][1]
                if x < 0 or x >= 8 or y < 0 or y >= 8:
                    break
                if [x, y] in queens:
                    ans.append([x, y])
                    break             
        return ans 
        