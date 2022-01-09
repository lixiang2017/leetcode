'''
The robot stays in the circle if and only if (looking at the final vector) it changes direction (ie. doesn't stay pointing north), or it moves 0.

Runtime: 39 ms, faster than 24.09% of Python3 online submissions for Robot Bounded In Circle.
Memory Usage: 14.3 MB, less than 49.85% of Python3 online submissions for Robot Bounded In Circle.
'''
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # dirs = ['N', 'W', "S", 'E']
        
        def change(face, x, y, instruct):
            if instruct == 'G':
                if face == 0:
                    y += 1
                elif face == 1:
                    x -= 1
                elif face == 2:
                    y -= 1
                elif face == 3:
                    x += 1
            elif instruct == 'L':
                face = (face + 1) % 4
            elif instruct == 'R':
                face = (face - 1) % 4
            return face, x, y
                
        face = x = y = 0
        for instruction in instructions:
            face, x, y = change(face, x, y, instruction)
            
        return (x == 0 and y == 0) or face != 0
        