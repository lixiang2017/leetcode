'''
只要为树的地方，都能通过
1是地面，不是树

sort + BFS

执行用时：5056 ms, 在所有 Python3 提交中击败了51.13% 的用户
内存消耗：15.7 MB, 在所有 Python3 提交中击败了36.36% 的用户
通过测试用例：54 / 54
'''

class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        m, n = len(forest), len(forest[0]) if forest else 0
        if 0 == forest[0][0]:
            return -1
        tree = []
        for i, row in enumerate(forest):
            for j, f in enumerate(row):
                if f > 1:
                    tree.append([f, i, j])

        tree.append([1, 0, 0])         
        tree.sort()

        def stepOfCut(si, sj, ei, ej, f) -> int:
            # start x, start y, end x, end y, height f 
            if si == ei and sj == ej:
                forest[si][sj] = 1
                return 0
            step = 0
            q = deque([(si, sj, step)])
            seen = set([(si, sj)])
            DIR = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            while q:
                i, j, step = q.popleft()
                for di, dj in DIR:
                    ni, nj = i + di, j + dj 
                    if 0 <= ni < m and 0 <= nj < n and forest[ni][nj] != 0 and (ni, nj) not in seen:
                        if ni == ei and nj == ej:
                            forest[ni][nj] = 1
                            return step + 1
                        seen.add((ni, nj))
                        q.append((ni, nj, step + 1))
            return -1
        
        tree_cnt = len(tree)
        ans = 0
        for idx in range(1, len(tree)):
            f1, si, sj = tree[idx - 1]
            f2, ei, ej = tree[idx]
            # print(si, sj, ei, ej, f2)
            step = stepOfCut(si, sj, ei, ej, f2)
            # print('step: ', step)
            if step == -1:
                return -1
            else:
                ans += step 
        return ans 

'''
[[1,2,3],[0,0,4],[7,6,5]]
[[1,2,3],[0,0,0],[7,6,5]]
[[2,3,4],[0,0,5],[8,7,6]]
[[54581641,64080174,24346381,69107959],[86374198,61363882,68783324,79706116],[668150,92178815,89819108,94701471],[83920491,22724204,46281641,47531096],[89078499,18904913,25462145,60813308]]
[[4,2,3],[0,0,1],[7,6,5]]
'''

