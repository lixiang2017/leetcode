'''
You are here!
Your runtime beats 73.53 % of python3 submissions.
You are here!
Your memory usage beats 39.93 % of python3 submissions.
'''

class Solution:
    def grayCode(self, n: int) -> List[int]:
        gray = [0]
        shift = 0
        for _ in range(n):
            for i in range(len(gray) - 1, -1, -1):
                gray.append(gray[i] + (1 << shift))
            shift += 1
        
        return gray
