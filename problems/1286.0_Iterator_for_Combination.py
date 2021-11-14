'''
Runtime: 48 ms, faster than 88.56% of Python3 online submissions for Iterator for Combination.
Memory Usage: 16.7 MB, less than 14.93% of Python3 online submissions for Iterator for Combination.
'''
class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.chars = characters
        self.L = len(characters)
        self.need = combinationLength
        self.coms = []
        self.dfs(0, 0, [])
        self.N = len(self.coms)
        self.it = 0
        self.coms.sort()
        
    def dfs(self, i: int, choose: int, seq: []) -> None:
        if choose == self.need:
            self.coms.append(''.join(seq))
            return 
        if i >= self.L:
            return        
        
        self.dfs(i + 1, choose, seq)
        self.dfs(i + 1, choose + 1, seq + [self.chars[i]])
        
    def next(self) -> str:
        seq = self.coms[self.it]
        self.it += 1
        return seq

    def hasNext(self) -> bool:
        return self.it < self.N


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()



'''
no need to use sort, just reverse

Runtime: 56 ms, faster than 61.69% of Python3 online submissions for Iterator for Combination.
Memory Usage: 16.6 MB, less than 35.82% of Python3 online submissions for Iterator for Combination.
'''
class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.chars = characters
        self.L = len(characters)
        self.need = combinationLength
        self.coms = []
        self.dfs(0, 0, [])
        self.N = len(self.coms)
        self.it = 0
        self.coms = self.coms[:: -1]
        
    def dfs(self, i: int, choose: int, seq: []) -> None:
        if choose == self.need:
            self.coms.append(''.join(seq))
            return 
        if i >= self.L:
            return        
        
        self.dfs(i + 1, choose, seq)
        self.dfs(i + 1, choose + 1, seq + [self.chars[i]])
        
    def next(self) -> str:
        seq = self.coms[self.it]
        self.it += 1
        return seq

    def hasNext(self) -> bool:
        return self.it < self.N


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()

