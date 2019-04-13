class Solution:
    def judgeCircle(self, moves: str) -> bool:
        return not any([sum([(m == 'R') - (m == 'L') for m in moves]), sum([(m == 'U') - (m == 'D') for m in moves])])


if __name__ == "__main__":
    moves = "UD"
    assert Solution().judgeCircle(moves)

    moves = "LL"
    assert not Solution().judgeCircle(moves)