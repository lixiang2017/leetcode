'''
凸包

执行用时：832 ms, 在所有 Python3 提交中击败了14.89% 的用户
内存消耗：15.4 MB, 在所有 Python3 提交中击败了96.81% 的用户
通过测试用例：87 / 87
'''
class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        n = len(trees)
        if n < 4:
            return trees 
        # find the left most point index 
        left_most = 0
        for i in range(1, n):
            if trees[i][0] < trees[left_most][0]:
                left_most = i 

        def cross(p: List[int], q: List[int], r: List[int]) -> int:
            '''
            p-->q, (qx - px, qy - py)
            q-->r, (rx - qx, ry - qy)
            '''
            return (q[0] - p[0]) * (r[1] - q[1]) - (q[1] - p[1]) * (r[0] - q[0])

        p = left_most
        seen = [False] * n 
        # seen[p] = True
        ans = []
        while True:
            q = (p + 1) % n 
            # p -- q -- r
            for r, (x, y) in enumerate(trees):
                if cross(trees[p], trees[q], trees[r]) < 0:
                    q = r 

            # check one line
            for i, s in enumerate(seen):
                if not s and p != i and q != i and cross(trees[p], trees[q], trees[i]) == 0:
                    ans.append(trees[i])
                    seen[i] = True
            if not seen[q]:
                seen[q] = True 
                ans.append(trees[q])
            p = q 
            if p == left_most:
                break 
        return ans 

