'''
Runtime: 46 ms, faster than 49.67% of Python3 online submissions for Minimum Flips to Make a OR b Equal to c.
Memory Usage: 16.3 MB, less than 25.27% of Python3 online submissions for Minimum Flips to Make a OR b Equal to c.
'''
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ans = 0
        while a or b or c:
            x, y, z = a & 1, b & 1, c & 1
            if z == 0:
                ans += x + y
            else:
                ans += 1 - (x | y)
            a >>= 1
            b >>= 1
            c >>= 1
        return ans 
        

'''
Runtime: 46 ms, faster than 49.67% of Python3 online submissions for Minimum Flips to Make a OR b Equal to c.
Memory Usage: 16.3 MB, less than 25.27% of Python3 online submissions for Minimum Flips to Make a OR b Equal to c.
'''
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        return bin((a | b) ^ c).count("1") + bin(a & b & ~c).count("1")


'''
Runtime: 44 ms, faster than 59.78% of Python3 online submissions for Minimum Flips to Make a OR b Equal to c.
Memory Usage: 16.2 MB, less than 68.57% of Python3 online submissions for Minimum Flips to Make a OR b Equal to c.
'''
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        return ((a | b) ^ c).bit_count() + (a & b & ~c).bit_count()
