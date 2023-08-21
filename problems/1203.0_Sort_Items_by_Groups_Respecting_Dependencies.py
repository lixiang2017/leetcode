'''
对-1的组重新编号

Runtime: 363 ms, faster than 85.88% of Python3 online submissions for Sort Items by Groups Respecting Dependencies.
Memory Usage: 44.5 MB, less than 22.03% of Python3 online submissions for Sort Items by Groups Respecting Dependencies.
'''
class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        # graph for group
        graph1 = defaultdict(set)
        # in degree for g1 -> g2, in_deg[g2] += 1
        in_deg = [0] * (n + m)
        group_nodes = set()
        # g1 -> g2
        for i, items in enumerate(beforeItems):
            if group[i] == -1:
                group[i] = m
                m += 1
            g2 = group[i]
            group_nodes.add(g2)
            for j in items:
                if group[j] == -1:
                    group[j] = m
                    m += 1
                g1 = group[j]
                if g2 == g1:
                    continue
                graph1[g1].add(g2)
                # will be duplicate
                # in_deg[g2] += 1

        for g1, items in graph1.items():
            for g2 in items:
                in_deg[g2] += 1

        # inter-group, check if groups respecting dependencies are feasible
        q = deque([x for x in group_nodes if in_deg[x] == 0])
        group_sequence = list(q)
        seen = set(q)
        while q:
            x = q.popleft()
            for child in graph1[x]:
                in_deg[child] -= 1
                if 0 == in_deg[child]:
                    q.append(child)
                    if child not in seen:
                        seen.add(child)
                        group_sequence.append(child)
                        
        if len(seen) != len(group_nodes):
            return []
        
        # intra-group, check if items in a group respecting dependencies are feasible
        ans = []
        # graph for items, group no -> items set
        graph2 = defaultdict(set)
        # in degree for items
        in_deg2 = [0] * n
        # j -> i
        # g1 -> g2
        # graph3 for items, item -> item
        graph3 = defaultdict(set)
        for i, items in enumerate(beforeItems):
            g2 = group[i]           
            for j in items:
                in_deg2[i] += 1
                graph3[j].add(i)
            graph2[g2].add(i)

        for g in group_sequence:
            seq = set(graph2[g])
            q2 = deque([x for x in seq if in_deg2[x] == 0])
            seen2 = set(q2)
            while q2:
                x = q2.popleft()
                ans.append(x)
                for child in graph3[x]:
                    in_deg2[child] -= 1
                    if child not in seen2 and 0 == in_deg2[child] and group[child] == g:
                        q2.append(child)
                        seen2.add(child)
            if len(seen2) != len(seq):
                return []
            
        return ans 
        
