class Solution:
    def processStr(self, s: str) -> str:
        res = []
        for c in s:
            match c:
                case "*":
                    if res:
                        res.pop()
                case "#":
                    res += res
                case "%":
                    res = res[:: -1]
                case _:
                    res.append(c)
        return ''.join(res)