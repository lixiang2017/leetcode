'''
approach: Logarithmatic Bounds + List
Time: O(MN), where M is int(log(bound, x)) and N is int(log(bound, y))
Space: O(MN)

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
approach: Logarithmatic Bounds + Set
Time: O(MN)
Space: O(MN)

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

'''
approach: Logarithmatic Bounds + Set
Time: O(MN)
Space: O(MN)

Runtime: 32 ms, faster than 68.44% of Python3 online submissions for Powerful Integers.
Memory Usage: 14.2 MB, less than 87.70% of Python3 online submissions for Powerful Integers.
'''

from math import log

class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        a = 1 if x == 1 else int(log(bound, x))
        b = 1 if y == 1 else int(log(bound, y))
        
        powerful_integers = set()
        for i in range(a + 1):
            for j in range(b + 1):
                value = x ** i + y ** j
                if value <= bound:
                    powerful_integers.add(value)
                else:
                    break
                
                if 1 == y:
                    break
            
            if 1 == x:
                break
        
        return list(powerful_integers)









