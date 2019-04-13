class Solution:
    def judgeCircle(self, moves: str) -> bool:
        if moves.count('R') == moves.count('L') and moves.count('U') == moves.count('D'):
            return True
        else:
            return False

if __name__ == "__main__":
    moves = "UD"
    assert Solution().judgeCircle(moves)

    moves = "LL"
    assert not Solution().judgeCircle(moves)