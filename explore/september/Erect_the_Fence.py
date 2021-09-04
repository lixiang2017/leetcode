'''
计算几何

You are here!
Your runtime beats 63.22 % of python3 submissions.
You are here!
Your memory usage beats 20.69 % of python3 submissions.

ref:
https://leetcode-cn.com/problems/erect-the-fence/solution/python-ji-suan-tu-bao-by-lycao/
'''
class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        N = len(trees)
        if N < 3:
            return trees
        
        points = sorted(set(tuple(t) for t in trees))
        cross = lambda o, a, b: (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
        
        low = []
        for p in points:
            while len(low) > 1 and cross(low[-2], low[-1], p) < 0:
                low.pop()
            low.append(tuple(p))
        
        up = []
        for p in reversed(points):
            while len(up) > 1 and cross(up[-2], up[-1], p) < 0:
                up.pop()
            up.append(tuple(p))
        return list(set(low + up))
        