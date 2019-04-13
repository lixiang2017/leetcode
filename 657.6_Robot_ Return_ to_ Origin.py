class Solution:
    def judgeCircle(self, moves: str) -> bool:
        return not sum(map({'U': 1, 'D': -1, 'L': -1j, 'R': 1j}.get, moves))
        
       
if __name__ == "__main__":
    moves = "UD"
    assert Solution().judgeCircle(moves)

    moves = "LL"
    assert not Solution().judgeCircle(moves)