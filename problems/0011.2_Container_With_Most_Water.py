'''
53 / 60 test cases passed.
    Status: Time Limit Exceeded

这样裁剪搜索空间还是不行。
python3不行，java可以通过。
'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n, ans = len(height), 0
        for i in range(1, n):
            if height[i] > ans // i:
                for j in range(i):
                    ans = max(ans, min(height[j], height[i]) * (i - j))
        return ans 


'''
greedy + two pointers
正确性需要证明
T: O(N)
S: O(1)

上面是裁剪搜索空间，双指针也是裁剪搜索空间。而且双指针是裁剪更多的搜索空间。

Runtime: 1054 ms, faster than 38.11% of Python3 online submissions for Container With Most Water.
Memory Usage: 27.5 MB, less than 58.32% of Python3 online submissions for Container With Most Water.
'''
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n, ans = len(height), 0
        i, j = 0, n - 1
        while i < j:
            ans = max(ans, min(height[i], height[j]) * (j - i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
            
        return ans 
        
