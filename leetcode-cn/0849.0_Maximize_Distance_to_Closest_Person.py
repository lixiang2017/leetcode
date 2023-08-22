'''
时间 68ms, 击败 26.53%使用 Python3 的用户
内存 16.48MB, 击败 61.22%使用 Python3 的用户
'''
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        i, j = 0, n - 1
        while i <= j and 0 == seats[i]:
            i += 1
        ans = i 
        while i <= j and 0 == seats[j]:
            j -= 1
        ans = max(ans, n - j - 1)
        while i <= j:
            while i <= j and 1 == seats[i]:
                i += 1
            k = i 
            while k <= j and 0 == seats[k]:
                k += 1
            ans = max(ans, (k - i + 1) // 2)
            i = k

        return ans 

