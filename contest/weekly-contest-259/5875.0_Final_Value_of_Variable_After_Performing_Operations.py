'''
AC
'''
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        c = Counter(operations)
        x += c["++X"] + c["X++"]
        x -= c["--X"]
        x -= c["X--"]
        return x