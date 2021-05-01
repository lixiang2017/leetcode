'''

You are here!
Your runtime beats 69.17 % of python3 submissions.
'''

class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        powerx = []
        powery = []
        px = 1
        while px <= bound:
            powerx.append(px)
            px *= x
            if 1 == x:
                break
                
        py = 1
        while py <= bound:
            powery.append(py)
            py *= y
            if 1 == y:
                break
        
        powers = []
        for px in powerx:
            for py in powery:
                if px + py <= bound:
                    powers.append(px + py)
                else:
                    break
        return list(set(powers))
 
'''
2
1
10
'''


'''
approach: Set

Runtime: 32 ms, faster than 68.44% of Python3 online submissions for Powerful Integers.
Memory Usage: 14.4 MB, less than 30.33% of Python3 online submissions for Powerful Integers.
'''

class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        powerx = []
        powery = []
        px = 1
        while px <= bound:
            powerx.append(px)
            px *= x
            if 1 == x:
                break
                
        py = 1
        while py <= bound:
            powery.append(py)
            py *= y
            if 1 == y:
                break
        
        powers = set()
        for px in powerx:
            for py in powery:
                if px + py <= bound:
                    powers.add(px + py)
                else:
                    break
        return list(powers)
 
'''
2
1
10
'''



