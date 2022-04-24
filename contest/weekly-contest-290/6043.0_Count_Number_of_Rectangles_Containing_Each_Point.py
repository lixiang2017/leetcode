'''
分桶排序+二分

执行用时：1664 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：30.8 MB, 在所有 Python3 提交中击败了100.00% 的用户
通过测试用例：47 / 47
'''
class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        rs = rectangles
        ps = points
        # height -> length list
        h2ls = [[] for _ in range(101)]
        for l, h in rs:
            h2ls[h].append(l)
        for h in range(101):
            h2ls[h].sort()
        
        ans = []
        for x, y in ps:
            cnt = 0
            for h in range(y, 101):
                idx = bisect.bisect_left(h2ls[h], x)
                cnt += len(h2ls[h]) - idx
            ans.append(cnt)
        
        return ans 

