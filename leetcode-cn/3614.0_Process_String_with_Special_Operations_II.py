class Solution:
    def processStr(self, s: str, k: int) -> str:
        l = 0
        for c in s:
            match c:
                case "*":
                    l = max(0, l - 1)
                case "#":
                    l *= 2
                case "%":
                    pass
                case _:
                    l += 1
        if l <= k:
            return '.'
        
        for c in reversed(s):
            match c:
                case '*':
                    l += 1
                case '#':
                    l //= 2
                    if k >= l:
                        k -= l
                case '%':
                    k = l - k - 1
                case _:
                    l -= 1
                    if l == k:
                        return c