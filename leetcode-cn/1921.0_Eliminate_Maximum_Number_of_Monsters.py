'''
140ms 击败 47.14%使用 Python3 的用户
29.81MB 击败 38.57%使用 Python3 的用户
'''
class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        n = len(dist)
        time = [(d + s - 1) // s for d, s in zip(dist, speed)]
        time.sort()
        for i, t in enumerate(time):
            if t <= i:
                return i
        return n 
