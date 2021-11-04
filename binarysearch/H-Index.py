'''
Sort + Binary Search
T: O(NlogN + logN)
S: O(1)

Your code took 30 milliseconds — faster than 99.50% in Python
'''
class Solution:
    def solve(self, citations):
        citations.sort()
        N = len(citations)
        l, r = 0, N - 1
        ans = 0
        while l <= r:
            mid = (l + r) // 2
            if citations[mid] >= N - mid:
                ans = N - mid
                r = mid - 1
            else:
                l = mid + 1
        return ans


'''
Your code took 32 milliseconds — faster than 94.49% in Python
'''
class Solution:
    def solve(self, citations):
        citations.sort()
        N = len(citations)
        l, r = 0, N - 1
        while l <= r:
            mid = (l + r) // 2
            if citations[mid] >= N - mid:
                r = mid - 1
            else:
                l = mid + 1
        return N - r - 1

'''
ans = N - mid
r = mid - 1
to remove `mid` ==> ans = N - r - 1
'''
