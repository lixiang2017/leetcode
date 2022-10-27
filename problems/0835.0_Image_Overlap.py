'''
Runtime: 1252 ms, faster than 46.20% of Python3 online submissions for Image Overlap.
Memory Usage: 14 MB, less than 75.44% of Python3 online submissions for Image Overlap.
'''
class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        ans = 0
        for di in range(-n + 1, n):
            for dj in range(-n + 1, n):
                total = 0
                for i in range(n):
                    if not (0 <= i + di < n):
                        continue
                    for j in range(n):
                        if not (0 <= j + dj < n):
                            continue
                        if img1[i + di][j + dj] == 1 and img2[i][j] == 1:
                            total += 1
                ans = max(ans, total)
        return ans 
        
        