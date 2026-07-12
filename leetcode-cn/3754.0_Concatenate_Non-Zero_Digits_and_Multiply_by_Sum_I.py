class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x, s, pow10 = 0, 0, 1
        while n:
            n, d = divmod(n, 10)
            if d > 0:
                x += d * pow10
                s += d
                pow10 *= 10
        return x * s


class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s = [ch for ch in str(n) if ch != '0']
        if not s:
            return 0
        x = int(''.join(s))
        _sum = sum(int(ch) for ch in s)
        return x * _sum