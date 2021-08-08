'''
LIS变形
Greedy + Binary Search
需要使用bisect_right寻找右边界，而非左边界。

78 / 78 个通过测试用例
状态：通过
执行用时: 232 ms
内存消耗: 28.4 MB
提交时间：6 小时前
'''

class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        q = []
        ans = []
        for o in obstacles:
            if not q or q[-1] <= o:
                q.append(o)
                ans.append(len(q))
            else:
                right = bisect_right(q, o)
                q[right] = o
                ans.append(right + 1)            
        
        return ans

