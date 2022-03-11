'''
bottom-up, from leaf to root, BFS

执行用时: 664 ms, 在所有 Python3 提交中击败了46.00% 的用户
内存消耗: 43.5 MB, 在所有 Python3 提交中击败了90.00% 的用户
内存消耗：119.9 MB, 在所有 Python3 提交中击败了25.27% 的用户
通过测试用例：206 / 206
'''
class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        n = len(parents)
        # from child to parent
        in_deg = [0] * n 
        # for every node, its children
        children = defaultdict(list)
        for child, p in enumerate(parents):
            if p != -1:
                in_deg[p] += 1
            children[p].append(child)

        q = deque([i for i, d in enumerate(in_deg) if d == 0])
        # nodes count for every node, its left subtree, right subtree and it self
        cnts = [1] * n
        while q:
            node = q.popleft()
            p = parents[node]
            if p == -1:
                continue
            cnts[p] += cnts[node]
            in_deg[p] -= 1
            if in_deg[p] == 0:
                q.append(p)

        score2cnt = defaultdict(int)
        max_score = 0
        for node in range(n):
            score = 1
            total = n - 1
            for child in children[node]:
                score *= cnts[child]
                total -= cnts[child]
            if total > 0:
                score *= total 

            score2cnt[score] += 1
            if score > max_score:
                max_score = score

        return score2cnt[max_score]
        


'''
DFS

执行用时：484 ms, 在所有 Python3 提交中击败了70.00% 的用户
内存消耗：119.9 MB, 在所有 Python3 提交中击败了25.27% 的用户
通过测试用例：206 / 206
'''
class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        n = len(parents)
        children = defaultdict(list)
        for node, p in enumerate(parents):
            children[p].append(node)

        max_score = cnt = 0
        def nodes_counter(node: int) -> int:
            score, total = 1, n - 1
            for child in children[node]:
                each_cnt = nodes_counter(child)
                score *= each_cnt
                total -= each_cnt
            if total > 0:
                score *= total 
            nonlocal max_score, cnt 
            if score > max_score:
                max_score, cnt = score, 1
            elif score == max_score:
                cnt += 1
            return n - total

        nodes_counter(0)
        return cnt 

