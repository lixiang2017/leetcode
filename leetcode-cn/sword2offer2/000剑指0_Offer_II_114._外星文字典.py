'''
topological sort

["wrt","wrf","er","ett","rftt"]
["z","x"]
["z","x","z"]
["z","z"]              # need to add all characters to graph
["ac","ab","zc","zb"]  # avoid duplicate increment for in_degree (c -> b)
["abc","ab"]           # wrong order, return ''
["wnlb"]               # just one word, return words[0] directly

执行用时：40 ms, 在所有 Python3 提交中击败了60.40% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了38.80% 的用户
通过测试用例：122 / 122


主站中是收费题目
注意：本题与主站 269 题相同： https://leetcode-cn.com/problems/alien-dictionary/
'''

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        if 1 == len(words):
            return words[0]
        # graph
        g = defaultdict(set)
        # in degree
        ind = defaultdict(int)
        # all chars, candidates
        cands = set()
        n = len(words)
        for i in range(1, n):
            w1, w2 = words[i - 1], words[i]
            # need to add all characters in w1 and w2
            for ch in w1:
                cands.add(ch)
            for ch in w2:
                cands.add(ch)
            # find first different ch
            j, size = 0, min(len(w1), len(w2))
            while j < size and w1[j] == w2[j]:
                j += 1
            # ["abc","ab"], wrong order!!!
            if j < len(w1) and j == len(w2):
                return ''
            if j == size:
                continue
            ch1, ch2 = w1[j], w2[j]  # ch1 -> ch2
            if ch2 not in g[ch1]:  # to avoid duplicate increment for in_degree
                g[ch1].add(ch2)
                ind[ch2] += 1

        q = deque([ch for ch in cands if 0 == ind[ch]])
        topo = list(q)
        while q:
            ch = q.popleft()
            for nxt in g[ch]:
                ind[nxt] -= 1
                if 0 == ind[nxt]:
                    q.append(nxt)
                    topo.append(nxt)

        if len(topo) == len(cands):
            return ''.join(topo)
        else:
            return ''


