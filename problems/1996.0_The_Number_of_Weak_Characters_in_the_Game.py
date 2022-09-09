'''
sort 

Runtime: 5199 ms, faster than 5.04% of Python3 online submissions for The Number of Weak Characters in the Game.
Memory Usage: 68.1 MB, less than 38.48% of Python3 online submissions for The Number of Weak Characters in the Game.
'''
class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        n = len(properties)
        properties.sort(key=lambda p: (-p[0], p[1]))
        max_d = properties[0][1]
        ans = 0
        for i in range(1, n):
            attack, defense = properties[i]
            if defense < max_d:
                ans += 1
            max_d = max(max_d, defense)
        return ans 


'''
sort 

Runtime: 2206 ms, faster than 96.21% of Python3 online submissions for The Number of Weak Characters in the Game.
Memory Usage: 68.3 MB, less than 23.33% of Python3 online submissions for The Number of Weak Characters in the Game.
'''
class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        n = len(properties)
        properties.sort(key=lambda p: (-p[0], p[1]))
        max_d = properties[0][1]
        ans = 0
        for i in range(1, n):
            attack, defense = properties[i]
            if defense < max_d:
                ans += 1
            else:
                max_d = max(max_d, defense)
        return ans 

