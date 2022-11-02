'''
Runtime: 43 ms, faster than 74.70% of Python3 online submissions for Minimum Genetic Mutation.
Memory Usage: 13.9 MB, less than 86.98% of Python3 online submissions for Minimum Genetic Mutation.
'''
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if start == end:
            return 0
        bank_set = set(bank)
        if end not in bank_set:
            return -1
        
        def diff(gene, mutataion):
            return sum(g != m for g, m in zip(gene, mutation))
        
        step = 0
        visited = set()
        q = [start]
        while q:
            next_q = []
            for gene in q:
                for mutation in bank:
                    if mutation not in visited and diff(gene, mutation) == 1:
                        if mutation == end:
                            return step + 1
                        visited.add(mutation)
                        next_q.append(mutation)
            q = next_q      
            step += 1
        return -1
        