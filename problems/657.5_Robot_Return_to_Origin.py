class Solution:
    def judgeCircle(self, moves: str) -> bool:
        direct = {'U': 1, 'D':-1, 'L': 1j, 'R': -1j}
        return 0 == sum(direct[m] for m in moves)

if __name__ == "__main__":
    moves = "UD"
    assert Solution().judgeCircle(moves)

    moves = "LL"
    assert not Solution().judgeCircle(moves)