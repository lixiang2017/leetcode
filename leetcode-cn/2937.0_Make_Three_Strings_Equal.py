class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        idx = -1
        for i, (a, b, c) in enumerate(zip(s1, s2, s3)):
            if a == b == c:
                idx = i
            else:
                break
        return -1 if idx == -1 else len(s1) + len(s2) + len(s3) - (idx + 1) * 3
    

class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        lcp = 0
        for x, y, z in zip(s1, s2, s3):
            if x != y or x != z:
                break
            lcp += 1
        return -1 if lcp == 0 else len(s1) + len(s2) + len(s3) - lcp * 3