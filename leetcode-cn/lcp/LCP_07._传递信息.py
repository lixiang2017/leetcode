'''
Hash Table + BFS

执行用时：40 ms, 在所有 Python3 提交中击败了80.67% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了71.85% 的用户
'''

class Solution:
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        pairs = defaultdict(set)
        for r0, r1 in relation:
            pairs[r0].add(r1)
        
        q = deque([0])
        step = choice = 0
        while q:
            step += 1
            for _ in range(len(q)):
                player = q.popleft()
                for partner in pairs[player]:
                    if step == k and partner == n - 1:
                        choice += 1
                    
                    q.append(partner)
                    
            if step == k:
                break

        return choice



'''
Hash Table + BFS

执行用时：40 ms, 在所有 Python3 提交中击败了80.67% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了50.84% 的用户
'''
class Solution:
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        pairs = defaultdict(set)
        for r0, r1 in relation:
            pairs[r0].add(r1)
        
        q = deque([0])
        while k:
            for _ in range(len(q)):
                player = q.popleft()
                for partner in pairs[player]:
                    q.append(partner)
            k -= 1

        return Counter(q)[n - 1]


'''
Hash Table + Counter

执行用时：44 ms, 在所有 Python3 提交中击败了67.23% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了61.76% 的用户
'''
class Solution:
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        pairs = defaultdict(set)
        for r0, r1 in relation:
            pairs[r0].add(r1)
        
        seen = Counter([0])
        while k:
            tries = Counter()
            for player, t in seen.items():
                for partner in pairs[player]:
                    tries[partner] += t
            seen = tries
            k -= 1

        return seen[n - 1]
