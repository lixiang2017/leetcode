'''
BFS

Runtime: 2387 ms, faster than 27.59% of Python3 online submissions for Find Closest Node to Given Two Nodes.
Memory Usage: 41.1 MB, less than 55.17% of Python3 online submissions for Find Closest Node to Given Two Nodes.
'''
class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        dist1 = {node1: 0}
        q1 = deque([(node1, 0)])
        while q1:
            node, step = q1.popleft()
            child = edges[node]
            if child not in dist1 and child != -1:
                dist1[child] = step + 1
                q1.append((child, step + 1))

        dist2 = {node2: 0}
        q2 = deque([(node2, 0)])
        while q2:
            node, step = q2.popleft()
            child = edges[node]
            if child not in dist2 and child != -1:
                dist2[child] = step + 1
                q2.append((child, step + 1))
        
        n = len(edges)
        ans = n
        max_dist = inf
        for i in range(n):
            if i in dist1 and i in dist2:
                m_dist = max(dist1[i], dist2[i])
                if m_dist < max_dist or (m_dist == max_dist and i < ans):
                    max_dist = m_dist
                    ans = i 
                    
        return ans if ans != n else -1
