'''
仅考虑左侧第一次出现字符的贡献
from left to right

left: (pos[d] or -1, i]
right: [i, n - 1]

Runtime: 528 ms, faster than 25.11% of Python3 online submissions for Total Appeal of A String.
Memory Usage: 14.9 MB, less than 74.30% of Python3 online submissions for Total Appeal of A String.
'''
class Solution:
    def appealSum(self, s: str) -> int:
        ans = 0
        n = len(s)
        pos = [-1] * 26
        for i, ch in enumerate(s):
            d = ord(ch) - ord('a')
            left = i - pos[d]
            right = n - i
            ans += left * right
            pos[d] = i 
        return ans 
    

'''
仅考虑右侧第一次出现字符的贡献
from right to left
left: [0, i]
right: [i, pos[d] or n)

Runtime: 382 ms, faster than 42.81% of Python3 online submissions for Total Appeal of A String.
Memory Usage: 15.2 MB, less than 33.53% of Python3 online submissions for Total Appeal of A String.
'''
class Solution:
    def appealSum(self, s: str) -> int:
        ans = 0
        n = len(s)
        pos = [n] * 26
        for i in range(n - 1, -1, -1):
            d = ord(s[i]) - ord('a')
            left = i + 1
            right = pos[d] - i
            ans += left * right
            pos[d] = i 
        return ans 
    

