import collections
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        c = collections.Counter(moves)
        return c['L'] == c['R'] and c['U'] == c['D']

if __name__ == "__main__":
    moves = "UD"
    assert Solution().judgeCircle(moves)

    moves = "LL"
    assert not Solution().judgeCircle(moves)