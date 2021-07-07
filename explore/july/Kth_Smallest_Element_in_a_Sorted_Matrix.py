'''
You are here!
Your runtime beats 14.30 % of python3 submissions.
You are here!
Your memory usage beats 93.49 % of python3 submissions.
'''

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        return sorted(chain(*matrix))[k - 1]