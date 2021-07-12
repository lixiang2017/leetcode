'''
One Loop,T:O(N),S:O(1)

执行用时：24 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：19 MB, 在所有 Python3 提交中击败了6.32% 的用户
'''
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        N = len(citations)
        h = 0
        for i in range(N - 1, -1, -1):
            if citations[i] >= N - i:
                h = N - i
            else:
                break
        
        return h


'''
Binary Search, T:O(logN),S:O(1)

执行用时：32 ms, 在所有 Python3 提交中击败了97.21% 的用户
内存消耗：18.9 MB, 在所有 Python3 提交中击败了37.55% 的用户
'''
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        N = len(citations)
        h = 0
        
        l, r = 0, N - 1
        while l <= r:
            mid = (r - l) // 2 + l
            if citations[mid] >= N - mid:
                r = mid - 1
                h = N - mid
            else:
                l = mid + 1
        
        return h
