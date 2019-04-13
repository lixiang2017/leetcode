class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x = 0
        y = 0
        for move in moves:
            if 'R' == move:
                x += 1
            elif 'L' == move:
                x -= 1
            elif 'U' == move:
                y += 1
            elif 'D' == move:
                y -= 1
                
        if 0 == x and 0 == y:
            return True
        else:
            return False

if __name__ == "__main__":
    moves = "UD"
    assert Solution().judgeCircle(moves)

    moves = "LL"
    assert not Solution().judgeCircle(moves)