'''
union find

Runtime: 904 ms, faster than 54.04% of Python3 online submissions for Smallest String With Swaps.
Memory Usage: 50.5 MB, less than 43.32% of Python3 online submissions for Smallest String With Swaps.
'''
class UnionFind:
    def __init__(self, n: int) -> None:
        self.n = n 
        self.p = list(range(n))
        # self.rank = [0] * n 
        self.size = [1] * n
        self.set_count = n 
    
    def find(self, x: int) -> int:
        if x == self.p[x]:
            return x 
        self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x: int, y: int) -> bool:
        px, py = self.find(x), self.find(y)
        if px == py:
            return False 
        # to make sure px >= py, so py -> px  
        if self.size[px] < self.size[py]:
            px, py = py, px 
        self.p[py] = px 
        self.size[px] += self.size[py]
        self.set_count -= 1
        return True 
            
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        uf = UnionFind(n)
        for a, b in pairs:
            uf.union(a, b)
        
        # group_id (root idx) -> children index list
        group2indices = defaultdict(list)
        for i in range(n):
            root_i = uf.find(i)
            group2indices[root_i].append(i)
        
        chars = list(s)
        for _, indices in group2indices.items():
            group = [chars[g] for g in indices]
            group.sort()
            indices.sort()
            for idx, char in zip(indices, group):
                chars[idx] = char 
        
        return ''.join(chars)
    
    
    
        
        
