'''
BFS

执行用时：32 ms, 在所有 Python3 提交中击败了86.74% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了97.44% 的用户
通过测试用例：14 / 14
'''
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank_set = set(bank)
        if end not in bank_set:
            return -1
        # (gene, step)
        q = deque([(start, 0)])
        seen = set([start])

        def diff(gene1: str, gene2: str) -> int:
            return sum(g1 != g2 for g1, g2 in zip(gene1, gene2))

        while q:
            gene, step = q.popleft()
            for b in bank_set:
                if b in seen:
                    continue
                if diff(gene, b) == 1:
                    if b == end:
                        return step + 1
                    seen.add(b)
                    # bank_set.remove(b) # cannot remove
                    q.append((b, step + 1))
        return -1
